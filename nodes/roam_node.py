#! /usr/bin/env python

from __future__ import with_statement
from __future__ import print_function

import roslib; roslib.load_manifest('multi_interface_roam') 
import rospy
import std_msgs.msg
import multi_interface_roam.multi_interface_roam as mir
import multi_interface_roam.rosmasterless
import sys
import os
import os.path
import time
import yaml
from diagnostic_msgs.msg import DiagnosticStatus, KeyValue, DiagnosticArray
from pr2_msgs.msg import AccessPoint

freq_to_chan_map = {
    2412000000 : 1, 
    2417000000 : 2, 
    2422000000 : 3, 
    2427000000 : 4, 
    2432000000 : 5, 
    2437000000 : 6, 
    2442000000 : 7, 
    2447000000 : 8, 
    2452000000 : 9, 
    2457000000 : 10, 
    2462000000 : 11, 
    2467000000 : 12, 
    2472000000 : 13, 
    2484000000 : 14, 
    3657500000 : 131, 
    3662500000 : 132, 
    3660000000 : 132, 
    3667500000 : 133, 
    3665000000 : 133, 
    3672500000 : 134, 
    3670000000 : 134, 
    3677500000 : 135, 
    3682500000 : 136, 
    3680000000 : 136, 
    3687500000 : 137, 
    3685000000 : 137, 
    3689500000 : 138, 
    3690000000 : 138, 
    4915000000 : 183, 
    4920000000 : 184, 
    4925000000 : 185, 
    4935000000 : 187, 
    4940000000 : 188, 
    4945000000 : 189, 
    4960000000 : 192, 
    4980000000 : 196, 
    5035000000 : 7, 
    5040000000 : 8, 
    5045000000 : 9, 
    5055000000 : 11, 
    5060000000 : 12, 
    5080000000 : 16, 
    5170000000 : 34, 
    5180000000 : 36, 
    5190000000 : 38, 
    5200000000 : 40, 
    5210000000 : 42, 
    5220000000 : 44, 
    5230000000 : 46, 
    5240000000 : 48, 
    5260000000 : 52, 
    5280000000 : 56, 
    5300000000 : 60, 
    5320000000 : 64, 
    5500000000 : 100, 
    5520000000 : 104, 
    5540000000 : 108, 
    5560000000 : 112, 
    5580000000 : 116, 
    5600000000 : 120, 
    5620000000 : 124, 
    5640000000 : 128, 
    5660000000 : 132, 
    5680000000 : 136, 
    5700000000 : 140, 
    5745000000 : 149, 
    5765000000 : 153, 
    5785000000 : 157, 
    5805000000 : 161, 
    5825000000 : 165, 
}

class MultiInterfaceDiagPublisher:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
           self.config = yaml.load(f.read())
        if 'wireless_namespace' in self.config:
            self.wireless_namespace = self.config['wireless_namespace']
        else:
            self.wireless_namespace = 'wifi'

        try:
            mir.logdir = self.config['log_directory']
        except KeyError:
            pass

#        console_output_file = os.path.join(mir.logdir, "console_output.log") 
#        try:
#            if self.config['redirect_console']:
#                print "Redirecting output to:", console_output_file
#                sys.stdout = open(console_output_file, "a", 1)
#                sys.stderr = sys.stdout
#        except KeyError:
#            pass
#        except IOError:
#            print "Error redirecting output to: ", console_output_file

        self.diag_pub = rospy.Publisher("/diagnostics", DiagnosticArray)
        self.wifi_pub = rospy.Publisher(self.wireless_namespace+"/accesspoint", AccessPoint)
        wireless_interfaces = []
        interfaces = self.config['interfaces'] 
        for i in interfaces:
            if interfaces[i]['type'] == 'wireless':
                wireless_interfaces.append(i)
        self.wifi_sub_pub = dict((iface, rospy.Publisher(self.wireless_namespace+"/"+iface+"/accesspoint", AccessPoint)) for iface in wireless_interfaces)

        self.hostname = os.uname()[1]
        print()
        print("**************************************************************")
        print(mir.log_time_string(time.time()), "restarting.")
        print("**************************************************************")
        mir.main(config_file, mir.SimpleSelectionStrategy, self.publish_diags)
        print("**************************************************************")
        print("Exiting.")
        print("**************************************************************")
        print()
        rospy.signal_shutdown("main has exited")

    @staticmethod
    def fill_diags(name, summary, hid, diags):
        ds = DiagnosticStatus()
        ds.values = [KeyValue(k, str(v)) for (k, v) in diags]
        ds.hardware_id = hid
        ds.name = rospy.get_caller_id().lstrip('/') + ": " + name
        ds.message = summary
        return ds
    
    @staticmethod
    def frequency_to_channel(freq):
        # A bit horrible, but will do until the message changes.
        try:
            return freq_to_chan_map[freq]
        except:
            return -1

    @staticmethod
    def gen_accesspoint_msg(iface):
        msg = AccessPoint()
        msg.essid = iface.essid
        msg.macaddr = iface.bssid
        msg.signal = iface.wifi_signal 
        msg.noise = iface.wifi_noise
        msg.snr = msg.signal - msg.noise
        msg.quality = iface.wifi_quality
        msg.rate = iface.wifi_rate
        msg.tx_power = iface.wifi_txpower
        msg.channel = MultiInterfaceDiagPublisher.frequency_to_channel(iface.wifi_frequency)
        return msg
    
    def publish_diags(self, strategy):
        now = rospy.get_rostime()
        ns = strategy.ns
        ds = self.fill_diags("synthetic interface", ns.diag_summary, self.hostname, strategy.ns.diags)
        ds.level = ns.diag_level
        statuses = [ds]

        for i in range(0, len(ns.interfaces)):
            iface = ns.interfaces[i]
            ds = self.fill_diags(iface.iface, iface.diag_summary, self.hostname, iface.diags)
            statuses.append(ds)
            if iface.__class__ == mir.WirelessInterface:
                msg = self.gen_accesspoint_msg(iface)
                msg.header.stamp = now
                self.wifi_sub_pub[iface.iface].publish(msg)
                if i == ns.active_iface:
                    self.wifi_pub.publish(msg)

        da = DiagnosticArray()
        da.header.stamp = rospy.get_rostime()
        da.status = statuses
        self.diag_pub.publish(da)
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
      print(file=sys.stderr)
      print("usage: roam_node.py config_file.yaml", file=sys.stderr)
      print(file=sys.stderr)
      print("This node cannot presently be used with roslaunch as it will be confused by the __name and __log parameters.", file=sys.stderr)
      sys.exit(1)
    
    rospy.init_node("multi_interface_roam", disable_rosout=True, disable_rostime=True, disable_signals=True)

    MultiInterfaceDiagPublisher(sys.argv[1])
