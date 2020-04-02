A demo FLASK integration between IFTTT and Firebase db

Here Im using Spotify trigger to give a Post req to my server hosted by ngrok.

My Spotify tigger TFTTT is as follows:
    1. Every time a song is added to my playlist a post req is sent to my server sending
        the required information such as
        a)SongPlaylist	b)Song_added	c)Song_added_by	d)Song_artist
    2. The data is then parsed and the coressponding data is sent to the firebase db and stored
    3. I parse the db and then display the stored results on a seperate api end point

Similary we can design many other web hooks integration to firebase

    DESIGN:
                                |IFTTT| ->>>> |FLASK| ->>>> |FIRE BASE|

Ps: the front design is a simple one , I was going for the logic implementation :p