class UserSideEffect:

    settings : dict

    def trigger_effect(self):

        raise TypeError("Effect of command must\
                         be defined by subclass.")


    def __init__(self, settings):

        if isinstance(self, ScreenSideEffect) or\
            isinstance(self, CheatSheetSideEffect) or\
            isinstance(self, CacheSideEffect):

            self.settings = settings

        else:

            raise TypeError("Every command must be a Screen,\
                             Cheatsheet, or cache command.")



class ScreenSideEffect(UserSideEffect):

    def __init__(self, settings):

        if 'screen' in super().settings.keys():

            super().__init__(settings)

        else:

            raise TypeError("ScreenSideEffect needs a Screen.")


class NullScrEff(ScreenSideEffect):

    def trigger_effect(self):
        return None

null_src_eff = NullScrEff({'screen' : None})



class CheatSheetSideEffect(UserSideEffect):

    def __init__(self, settings):

        if 'cheatsheet' in super().settings.keys():

            super().__init__(settings)

        else:

            raise TypeError("CheatSheetSideEffect needs a CheatSheet.")


class NullCheEff(CheatSheetSideEffect):

    def trigger_effect(self):
        return None

null_che_eff = NullCheEff({'cheatsheet' : None})



class CacheSideEffect(UserSideEffect):

    def __init__(self, settings):

        if 'cache' in super().settings.keys():
            
            super().__init__(settings)
            self.cs = super().settings['cache']

        else:

            raise TypeError("CacheSideEffect needs a Cache.")


class NullCacEff(CacheSideEffect):

    def trigger_effect(self):
        return None

null_cac_eff = NullCacEff({'cache' : None})



class Command:

    def __init__(self,
        cheatsheet_effect : CheatSheetEffect = null_che_eff,
        cache_effect : NullCacheEffect = null_cac_eff,
        screen_effect : ScreenSideEffect = null_scr_eff):

        self.cheatsheet_effect = cheatsheet_effect
        self.cache_effect = cache_effect
        self.screen_effect = screen_effect

    def run(self):

        self.cheatsheet_effect.trigger_effect()
        self.cache_effect.trigger_effect()
        self.screen_effect.trigger_effect()

