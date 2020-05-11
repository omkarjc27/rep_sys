**Note**: All the names and the API-calls that I've used are just placeholders, everything should be re-iterated obviously. Also the Errors should be given ErrorCodes, currently they just say what's wrong.

## General Working
For a reputation system that records accross communities and which will be open to every community/team, it has to ensure that a user should not himself create a community and award themselves a lot of points. Also it has to make sure that score is transferable 

i.e. 
if ```A``` has a reputation score of ```100``` in a ```community of 100 people```   
& ```B``` has a a reputation score of ```100``` in a ```community of 20 people```

Then ```A``` has a better reputation than ```B```, hence ```A``` should be ranked higher.

For this, I propose a system.
The system will have two types of score
1. **Local Score**: Array of Scores of a user, in different communities.
2. **Global Score** : A single number which will be calculated form the user's local score.

Every user will have a db of local scores for every community they are a part of.

When a user makes contribution to the community in any way (it might be comments,upvotes,posts,code submission,etc..) then the community will award the user with one upvote/point.

Which will get added to the local score of that user, for that given community.So the local score will increase by 1.

But also it will add to the global score of the user, But the global score will be incremented by the [h-index](#h-index) of that community at that point in time.

### h-index
[Read About it here.](https://en.wikipedia.org/wiki/H-index)

In this system the h-index of a community is the highest value of ```h```

Where 

    h number of users in a community have atleast h local score points.

So more the number of people with a lot of votes in a community more it's h-index will be.

This will take care of the problems stated above.

The only problem that will remain is that a user might create a community where they might keep on adding other users and giving them points 

eg. I might create a community and add 100 users to it and give each of them 100 points that would make my community's h-index 100

Solution to this is restricting the api usage of a given api_key by time like``` x requests per minute.```

```
In The Code
product_list is the list of global scores
user_list is the list of local scores
```


## cURL API Interface

### List Of API methods
**These API methods should be initially restricted only for the homepage of the platform, where the users can create accounts or communities**
- [**Create a Community**](#create-a-community)
- [**Create a User Account**](#create-a-user-account)


**These Methods must be Accesible to Public**
- [**Add User To A Community**](#add-user-to-a-community)
- [**Award/UpVote a User on Your Community**](#award-1-point-to-a-user)
- [**Show Community Info**](#show-community-info)
- [**Show User Info**](#show-user-info)



### Create a User Account

**Base URL:**```https://rep-sys.herokuapp.com```

**Request :**
```
curl base_url/user/create/ \
    -X POST \
    -d  '{"username" : "sample_user_name", "email" : "sample_email@mail.com"}' \
    -H "Content-Type: application/json"
```

**Ideal Response :**```'Successful'```

**Errors**
- ```Username Already in Use```
- ```Email Already in Use```

### Create a Community
```
curl base_url/community/create/ \
    -X POST \
    -d '{"community_name" : "sample_community_name","email" : "community_email@mail.com","desc" : "Description of the community...."}' \
    -H "Content-Type: application/json"
```

**Ideal Response :** ```Your_community's_API_KEY```


**Errors**
- ```Community Name Already in Use```
- ```Email Already in Use```

### Add User To A Community

**Request :**
```
curl base_url/community/add_user/ \
    -X POST \
    -d '{"username" : "sample_user_name"}' \
    -H "THE_API_KEY:Your_API_key" \
    -H "Content-Type: application/json"
```

**Ideal Response :**
```Successful```

**Errors**
- ```Invalid API_KEY```
- ```Username Does Not Exist```


### Show Community Info

**Request :**
```
curl base_url/community/ \
        -X GET \
        -H "THE_API_KEY:Your_API_key"
```

**Ideal Response :**
```
/* All usernames with their corresponding points only from your community*/
{
    'username1':'x-points',
    'username2':'y-points',
    ...
    'username3':'z-points',
}
```

**Errors**
- ```Invalid API_KEY```




### Award 1 Point to a User

**Request :**
```
curl base_url/user/award/ \
    -X POST \
    -d '{"username" : "sample_user_name"}' \
    -H "THE_API_KEY:Abxz7531....."
    -H "Content-Type: application/json"
```

**Ideal Response :**
```Successful```

**Errors**
- ```Invalid API_KEY```
- ```Username not in your community```


### Show User Info

**Request :**
```
curl base_url/user/<username> -X GET
```

**Ideal Response :**
```
{
    'total_score' : 738, \\ The Global Score total
    'community_wise':{    \\ The Global Scores for all the communities they have been or are a part of
        'community_name1': 32,
        'community_name2': 47,        
        ...

        'community_name3': 58,
    }
}
```

**Errors**
- ```Invalid Username```
