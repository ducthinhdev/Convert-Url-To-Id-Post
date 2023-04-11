import requests,time
def converLinktoUid(link):
    if 'groups' in link:
        # Check Post Group Có Sẵn ID
        if link.split('https://www.facebook.com/groups/')[1].split('/post')[0].isdigit():
            grID = link.split('https://www.facebook.com/groups/')[1].split('/post')[0]
            # r = requests.post('https://id.atpsoftware.vn/',data={'linkCheckUid':link}).text
            idpost = str(grID)+'_'+link.split('posts/')[1].split('/')[0]
            return idpost
        # Check Post Group Không Có Id 
        else:
            grUS = 'https://www.facebook.com/groups/'+ link.split('https://www.facebook.com/groups/')[1].split('/post')[0]
            grID = requests.post('https://id.atpsoftware.vn/',data={'linkCheckUid':grUS}).text.split('hidden;">')[1].split('<')[0]
            idpost = str(grID)+'_'+ link.split('posts/')[1].split('/')[0]
            return idpost
    # Post ID Người Dùng
    elif 'id=' in link:
        idacc = link.split('&id=')[1]
        id = requests.post('https://id.traodoisub.com/api.php',data={'link':link}).json()['id']
        idpost = idacc+'_'+str(id)
        return idpost
    # Post ID Page
    else:
        # Lay USERNAME
        postUS = 'https://www.facebook.com/'+link.split('https://www.facebook.com/')[1].split('/posts')[0]
        getuserID = requests.post('https://id.traodoisub.com/api.php',data={'link':postUS}).json()
        if 'error' in getuserID:
            print('URL Không Tồn Tại !')
        else:
            userID = getuserID['id']
            time.sleep(1)
            postID = requests.post('https://id.traodoisub.com/api.php',data={'link':link}).json()['id']
            idpost = str(userID)+'_'+ str(postID)
            return idpost
print(converLinktoUid('https://www.facebook.com/C1DoLa24h/posts/pfbid0UkEUwasfiYa75CgpU14cEpLuo94fMdTPHfHLE59vfM4jtDodeCo63V1kR6uBuNPkl'))
