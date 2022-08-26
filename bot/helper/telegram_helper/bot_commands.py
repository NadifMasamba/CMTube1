from bot import CMD_INDEX
import os
def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command


class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand(f'START_COMMAND', f'msbstart{CMD_INDEX}')
        self.MirrorCommand = getCommand('MIRROR_COMMAND', f'msb{CMD_INDEX}')
        self.UnzipMirrorCommand = getCommand('UNZIP_COMMAND', f'msbunzip{CMD_INDEX}')
        self.ZipMirrorCommand = getCommand('ZIP_COMMAND', f'msbzip{CMD_INDEX}')
        self.CancelMirror = getCommand('CANCEL_COMMAND', f'msbcancel{CMD_INDEX}')
        self.CancelAllCommand = getCommand('CANCEL_ALL_COMMAND', f'msbcancelall{CMD_INDEX}')
        self.ListCommand = getCommand('LIST_COMMAND', f'msblist{CMD_INDEX}')
        self.SearchCommand = getCommand('SEARCH_COMMAND', f'msbsearch{CMD_INDEX}')
        self.StatusCommand = getCommand('STATUS_COMMAND', f'msbstatus{CMD_INDEX}')
        self.AuthorizedUsersCommand = getCommand('USERS_COMMAND', f'msbusers{CMD_INDEX}')
        self.AuthorizeCommand = getCommand('AUTH_COMMAND', f'msbauthorize{CMD_INDEX}')
        self.UnAuthorizeCommand = getCommand('UNAUTH_COMMAND', f'msbunauthorize{CMD_INDEX}')
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', f'msbaddsudo{CMD_INDEX}')
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', f'msbrmsudo{CMD_INDEX}')
        self.PingCommand = getCommand('PING_COMMAND', f'msbping{CMD_INDEX}')
        self.RestartCommand =  getCommand('RESTART_COMMAND', f'msbrestart{CMD_INDEX}')
        self.StatsCommand = getCommand('STATS_COMMAND', f'msbstats{CMD_INDEX}')
        self.HelpCommand = getCommand('HELP_COMMAND', f'msbhelp{CMD_INDEX}')
        self.LogCommand = getCommand('LOG_COMMAND', f'msblog{CMD_INDEX}')
        self.BtSelectCommand = getCommand('BTSEL_COMMAND', f'msbbtsel{CMD_INDEX}')
        self.SpeedCommand = getCommand('SPEEDTEST_COMMAND', f'msbspeedtest{CMD_INDEX}')
        self.CloneCommand = getCommand('CLONE_COMMAND', f'msbclone{CMD_INDEX}')
        self.CountCommand = getCommand('COUNT_COMMAND', f'msbcount{CMD_INDEX}')
        self.WatchCommand =  getCommand('WATCH_COMMAND', f'msbwatch{CMD_INDEX}')
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', f'msbzipwatch{CMD_INDEX}')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', f'msbqb{CMD_INDEX}')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_COMMAND', f'msbqbunzip{CMD_INDEX}')
        self.QbZipMirrorCommand = getCommand('QBZIP_COMMAND', f'msbqbzip{CMD_INDEX}')
        self.DeleteCommand = getCommand('DELETE_COMMAND', f'msbdel{CMD_INDEX}')
        self.ShellCommand = getCommand('SHELL_COMMAND', f'msbshell{CMD_INDEX}')
        self.ExecHelpCommand = getCommand('EXEHELP_COMMAND', f'msbexechelp{CMD_INDEX}')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', f'msbleechset{CMD_INDEX}')
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', f'msbsetthumb{CMD_INDEX}')
        self.UsageCommand = getCommand('USAGE_COMMAND', f'msbusage{CMD_INDEX}')
        self.LeechCommand = getCommand('LEECH_COMMAND', f'msbleech{CMD_INDEX}')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', f'msbunzipleech{CMD_INDEX}')
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', f'msbzipleech{CMD_INDEX}')
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', f'msbqbleech{CMD_INDEX}')
        self.QbUnzipLeechCommand = getCommand('QBZIPLEECH_COMMAND', f'msbqbunzipleech{CMD_INDEX}')
        self.QbZipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', f'msbqbzipleech{CMD_INDEX}')
        self.LeechWatchCommand = getCommand('LEECHWATCH_COMMAND',  f'msbleechwatch{CMD_INDEX}')
        self.MediaInfoCommand = getCommand('MEDIAINFO_COMMAND', f'msbmediainfo{CMD_INDEX}')
        self.HashCommand = getCommand('HASH_COMMAND', f'msbhash{CMD_INDEX}')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', f'msbleechzipwatch{CMD_INDEX}')
        self.RssListCommand = getCommand('RSSLIST_COMMAND', f'msbrsslist{CMD_INDEX}')
        self.RssGetCommand = getCommand('RSSGET_COMMAND', f'msbrssget{CMD_INDEX}')
        self.RssSubCommand = getCommand('RSSSUB_COMMAND', f'msbrsssub{CMD_INDEX}')
        self.RssUnSubCommand = getCommand('RSSUNSUB_COMMAND', f'msbrssunsub{CMD_INDEX}')
        self.RssSettingsCommand = getCommand('RSSSET_COMMAND', f'msbrssset{CMD_INDEX}')
        self.WayBackCommand = getCommand('WAYBACK_COMMAND', f'msbwayback{CMD_INDEX}')
        self.EvalCommand = f'msbeval{CMD_INDEX}'
        self.ExecCommand = f'msbexec{CMD_INDEX}'
        self.ClearLocalsCommand = f'msbclearlocals{CMD_INDEX}'
        self.SleepCommand = getCommand('SLEEP_COMMAND', f'msbsleep{CMD_INDEX}')

BotCommands = _BotCommands()
