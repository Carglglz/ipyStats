# @Author: carlosgilgonzalez
# @Date:   2019-11-13T15:47:18+00:00
# @Last modified by:   carlosgilgonzalez
# @Last modified time: 2019-11-13T18:05:51+00:00

import subprocess
import shlex


class ISTATS:
    def __init__(self):
        self.cmd = {'cpu_temp': 'istats cpu --no-graphs',
                    'palmr_temp': 'istats scan Ts0P',
                    'fan_speed': 'istats fan speed --no-graphs',
                    'batt_health': 'istats battery health',
                    'batt_time': 'istats battery time',
                    'batt_temp': 'istats battery temp',
                    'batt_charge': 'istats battery charge'}
        self.cmd_rev = {v: k for k, v in self.cmd.items()}

    def _get_output_key(self, raw):
        shcmd = shlex.split(raw)
        _rw = subprocess.check_output(shcmd).decode()
        data = float(_rw.strip().split(' ')[-1][:-2])
        unit = (_rw.strip().split(' ')[-1][-2:])
        return ({self.cmd_rev[raw]: data, 'unit': unit})

    def _get_stat_rawkey(self, raw, unit):
        shcmd = shlex.split(raw)
        data = float(subprocess.check_output(
            shcmd).decode().strip().split(' ')[-1][:-2])
        return ({self.cmd_rev[raw]: data, 'unit': unit})

    def get_stat_l(self, raw):
        shcmd = shlex.split(raw)
        speed = subprocess.check_output(shcmd).decode().strip().split('\n')
        fan_dict = {fan.strip().split(':')[0]: fan.strip().split(
            ':')[-1].strip() for fan in speed}
        return fan_dict

    def get_stat(self, raw):
        shcmd = shlex.split(raw)
        btime = subprocess.check_output(shcmd).decode().strip().split(' ')[-1]
        label = subprocess.check_output(shcmd).decode().strip().split(':')[0]
        return {label: btime}

    def batt_time(self, raw=False):
        if not raw:
            return self.get_stat(self.cmd['batt_time'])
        else:
            return list(self.get_stat(self.cmd['batt_time']).values())[0]

    def batt_charge(self):
        return self.get_stat_l(self.cmd['batt_charge'])

    def batt_temp(self):
        return self.get_stat_l(self.cmd['batt_temp'])

    def cpu_temp(self, raw=False):

        if not raw:
            return self.get_stat(self.cmd['cpu_temp'])
        else:
            return self._get_output_key(self.cmd['cpu_temp'])

    def palmr_temp(self, raw=False):
        if not raw:
            result = self._get_stat_rawkey(self.cmd['palmr_temp'], 'ºC')
            val = {'palmr_temp': "{} {}".format(
                result['palmr_temp'], result['unit'])}
            return val

        else:
            return self._get_stat_rawkey(self.cmd['palmr_temp'], 'ºC')

    def fan_speed(self):
        return self.get_stat_l(self.cmd['fan_speed'])


istat = ISTATS()
