import instaloader,statistics


L = instaloader.Instaloader() 
profiles=[]
profil=input("Pes mou to username tou instagram pou thes: ")
print(profil,type(profil))
profile = instaloader.Profile.from_username(L.context, profil) 
print(profile.get_posts())
count=0
for post in profile.get_posts():
    if(count==100):
        break
    post_comments = post.get_comments()

    for comment in post_comments:
        profiles.append(comment.owner.username)
    count+=1
profiles.sort() #tin ekana sort gia na me diefkolini na kano elenxo an to apotelesma einai sosto sto telos
print(profiles) #kai afto to afino edo gia na deite oti einai sosto to apotelesma, an den to xreiazeste sbiste to
maxcommentprofile=statistics.mode(profiles)
print("O xrhsths tou instagram me onoma: ",maxcommentprofile,"exei kanei ta perisotera sxolia sto profil tou/ths: ",profil)

