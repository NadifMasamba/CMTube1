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
        self.StartCommand = getCommand(f'START_COMMAND', f'peastart{CMD_INDEX}')
        self.MirrorCommand = getCommand('MIRROR_COMMAND', f'pea{CMD_INDEX}')
        self.UnzipMirrorCommand = getCommand('UNZIP_COMMAND', f'peaunzip{CMD_INDEX}')
        self.ZipMirrorCommand = getCommand('ZIP_COMMAND', f'peazip{CMD_INDEX}')
        self.CancelMirror = getCommand('CANCEL_COMMAND', f'peacancel{CMD_INDEX}')
        self.CancelAllCommand = getCommand('CANCEL_ALL_COMMAND', f'peacancelall{CMD_INDEX}')
        self.ListCommand = getCommand('LIST_COMMAND', f'pealist{CMD_INDEX}')
        self.SearchCommand = getCommand('SEARCH_COMMAND', f'peasearch{CMD_INDEX}')
        self.StatusCommand = getCommand('STATUS_COMMAND', f'peastatus{CMD_INDEX}')
        self.AuthorizedUsersCommand = getCommand('USERS_COMMAND', f'peausers{CMD_INDEX}')
        self.AuthorizeCommand = getCommand('AUTH_COMMAND', f'peaauthorize{CMD_INDEX}')
        self.UnAuthorizeCommand = getCommand('UNAUTH_COMMAND', f'peaunauthorize{CMD_INDEX}')
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', f'peaaddsudo{CMD_INDEX}')
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', f'pearmsudo{CMD_INDEX}')
        self.PingCommand = getCommand('PING_COMMAND', f'peaping{CMD_INDEX}')
        self.RestartCommand =  getCommand('RESTART_COMMAND', f'pearestart{CMD_INDEX}')
        self.StatsCommand = getCommand('STATS_COMMAND', f'peastats{CMD_INDEX}')
        self.HelpCommand = getCommand('HELP_COMMAND', f'peahelp{CMD_INDEX}')
        self.LogCommand = getCommand('LOG_COMMAND', f'pealog{CMD_INDEX}')
        self.BtSelectCommand = getCommand('BTSEL_COMMAND', f'peabtsel{CMD_INDEX}')
        self.SpeedCommand = getCommand('SPEEDTEST_COMMAND', f'peaspeedtest{CMD_INDEX}')
        self.CloneCommand = getCommand('CLONE_COMMAND', f'peaclone{CMD_INDEX}')
        self.CountCommand = getCommand('COUNT_COMMAND', f'peacount{CMD_INDEX}')
        self.WatchCommand =  getCommand('WATCH_COMMAND', f'peawatch{CMD_INDEX}')
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', f'peazipwatch{CMD_INDEX}')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', f'peaqb{CMD_INDEX}')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_COMMAND', f'peaqbunzip{CMD_INDEX}')
        self.QbZipMirrorCommand = getCommand('QBZIP_COMMAND', f'peaqbzip{CMD_INDEX}')
        self.DeleteCommand = getCommand('DELETE_COMMAND', f'peadel{CMD_INDEX}')
        self.ShellCommand = getCommand('SHELL_COMMAND', f'peashell{CMD_INDEX}')
        self.ExecHelpCommand = getCommand('EXEHELP_COMMAND', f'peaexechelp{CMD_INDEX}')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', f'pealeechset{CMD_INDEX}')
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', f'peasetthumb{CMD_INDEX}')
        self.UsageCommand = getCommand('USAGE_COMMAND', f'peausage{CMD_INDEX}')
        self.LeechCommand = getCommand('LEECH_COMMAND', f'pealeech{CMD_INDEX}')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', f'peaunzipleech{CMD_INDEX}')
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', f'peazipleech{CMD_INDEX}')
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', f'peaqbleech{CMD_INDEX}')
        self.QbUnzipLeechCommand = getCommand('QBZIPLEECH_COMMAND', f'peaqbunzipleech{CMD_INDEX}')
        self.QbZipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', f'peaqbzipleech{CMD_INDEX}')
        self.LeechWatchCommand = getCommand('LEECHWATCH_COMMAND',  f'pealeechwatch{CMD_INDEX}')
        self.MediaInfoCommand = getCommand('MEDIAINFO_COMMAND', f'peamediainfo{CMD_INDEX}')
        self.HashCommand = getCommand('HASH_COMMAND', f'peahash{CMD_INDEX}')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', f'pealeechzipwatch{CMD_INDEX}')
        self.RssListCommand = getCommand('RSSLIST_COMMAND', f'pearsslist{CMD_INDEX}')
        self.RssGetCommand = getCommand('RSSGET_COMMAND', f'pearssget{CMD_INDEX}')
        self.RssSubCommand = getCommand('RSSSUB_COMMAND', f'pearsssub{CMD_INDEX}')
        self.RssUnSubCommand = getCommand('RSSUNSUB_COMMAND', f'pearssunsub{CMD_INDEX}')
        self.RssSettingsCommand = getCommand('RSSSET_COMMAND', f'pearssset{CMD_INDEX}')
        self.WayBackCommand = getCommand('WAYBACK_COMMAND', f'peawayback{CMD_INDEX}')
        self.EvalCommand = f'peaeval{CMD_INDEX}'
        self.ExecCommand = f'peaexec{CMD_INDEX}'
        self.ClearLocalsCommand = f'peaclearlocals{CMD_INDEX}'
        self.SleepCommand = getCommand('SLEEP_COMMAND', f'peasleep{CMD_INDEX}')

BotCommands = _BotCommands()
