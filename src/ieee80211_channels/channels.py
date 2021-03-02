#! /usr/bin/env python

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

class IEEE80211_Channels:
    """
    This class implements IEEE802.11 frequency <---> (channel, band) mapping.
    """
    BAND_2400_MHz = "2400MHz band" #: 2.4GHz band
    BAND_3600_MHz = "3600MHz band" #: 3.6GHz band
    BAND_5000_MHz = "5000MHz band" #: 5GHz band
    BAND_UNKNOWN = "Unknown band"  #: unknown band

    @staticmethod
    def get_band_from_freq(freq):
        """
        Retrieves the band a frequency belongs to.

        @type freq: long
        @param freq: the frequency in Hz

        @rtype: string
        @return: the frequency band (see the class constants)
        """
        if freq >= 2412000000 and freq <= 2484000000: 
            return IEEE80211_Channels.BAND_2400_MHz
        elif freq >= 3657500000 and freq <= 3690000000:
            return IEEE80211_Channels.BAND_3600_MHz
        elif freq >= 4915000000 and freq <= 5825000000:
            return IEEE80211_Channels.BAND_5000_MHz
        else:
            return IEEE80211_Channels.BAND_UNKNOWN

    @staticmethod
    def get_channel(freq):
        """
        Returns the channel number corresponding to a frequency.
        
        @type freq: long
        @param freq: the frequency in Hz

        @rtype: int
        @return: channel number or -1 if the frequency is not a valid IEEE802.11 channel
        """
        try:
            return freq_to_chan_map[freq]
        except:
            return -1

    @staticmethod
    def get_freq(channel, band):
        """
        Returns the frequency corresponding to a given channel and band.
        
        @type channel: int
        @param channel: the channel number
        @type band: string
        @param band: the frequency band (one of the class defined constants should be given)

        @rtype: long
        @return: frequency in Hz or -1 if the (channel, band) combination is not valid
        """
        for freq, ch in freq_to_chan_map.iteritems():
            if ch == channel and IEEE80211_Channels.get_band_from_freq(freq) == band:
                return freq
        return -1
