# Imports from this project
from kolreq.kolreq import clear
from shared.Audio import audio_shared


def Audio(call):
    clear()
    print(f"cookie={call.settings.Youtubedl.cookie}")
    print("link to audio, playlist, 0. GoBack")
    url = input("#")
    if(url == "0"):
        clear()
        call.name()
    else:
        print("<Enter> a single audio, \n" +
              "1. to download full playlist or follow example 1-3,7,9")
        numb = input("#")
        if numb == "1":
            items = ""
        else:
            items = numb

        cmd = audio_shared(url, bool(numb), items, call.floc, call.settings.Youtubedl.audioDir, call.settings.Youtubedl.cookie)

        print("starting youtube-dl please wait...")

        call.process_start(cmd)

        print("\a")
