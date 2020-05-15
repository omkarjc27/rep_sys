---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell
  - ruby
  - python
  - javascript

toc_footers:
  - <a href='#'>Sign Up for a Developer Key</a>
  - <a href='https://github.com/slatedocs/slate'>Documentation Powered by Slate</a>

includes:
  - errors

search: true
---

# Introduction
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

## h-index
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

# Apps
## Discord

Integrating into a Discord community is easy...(to be updated)

## Reddit

Integrating into a Reddit community is easy...(to be updated)

# Web API

**These API methods should be initially restricted only for the homepage of the platform, where the users can create accounts or communities**

**Base URL:**```https://rep-sys.herokuapp.com```

## Authenticating
Details on obtaining an API key for the web api approach of integrating into community.

## Create User

```shell
curl base_url/users/ \
    -X PUT \
    -d  '{"username" : "sample_user_name", "email" : "sample_email@mail.com"}' \
    -H "Content-Type: application/json"
    -H "Authorization: auth-scheme-to-be-added"
```

> The above command returns JSON structured like this:

```json
[
  {
    "id": 1,
    "name": "Fluffums",
    "breed": "calico",
    "fluffiness": 6,
    "cuteness": 7
  },
  {
    "id": 2,
    "name": "Max",
    "breed": "unknown",
    "fluffiness": 5,
    "cuteness": 10
  }
]
```

This endpoint creates a user account.

### HTTP Request

`PUT <BaseEnpoint>/users/`

## Create Community

```shell
curl base_url/community/ \
    -X PUT \
    -d '{"community_name" : "sample_community_name","email" : "community_email@mail.com","desc" : "Description of the community...."}' \
    -H "Content-Type: application/json"
    -H "Authorization: meowmeowmeow"
```

This endpoint creates a community.

> The above command returns JSON structured like this:

```json
[
  {
    "id": 1,
    "name": "Fluffums",
    "breed": "calico",
    "fluffiness": 6,
    "cuteness": 7
  },
  {
    "id": 2,
    "name": "Max",
    "breed": "unknown",
    "fluffiness": 5,
    "cuteness": 10
  }
]
```

### HTTP Request

`PUT <BaseEnpoint>/community/`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
include_cats | false | If set to true, the result will also include cats.
available | true | If set to false, the result will include kittens that have already been adopted.

## Add User To Community

```shell
curl base_url/community/<username> \
    -X POST \
    -H "THE_API_KEY:Your_API_key"
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "name": "Max",
  "breed": "unknown",
  "fluffiness": 5,
  "cuteness": 10
}
```

This endpoint adds a user to community.

### HTTP Request

`POST <BaseEnpoint>/community/<username>`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the kitten to retrieve

## Show Community Info

```shell
curl base_url/community/ \
        -X GET \
        -H "THE_API_KEY:Your_API_key"
```

> The above command returns JSON structured like this:

```json
{
    "username1":"x-points",
    "username2":"y-points",
    "username3":"z-points",
}
```

This endpoint gets community info.

### HTTP Request

`GET <BaseEnpoint>/community`

## Award 1 Point to User

```shell
curl base_url/award/<username> \
    -X POST \
    -H "THE_API_KEY:Your_API_KEY"
```

> The above command returns JSON structured like this:

```json
{
    "username1":"x-points",
    "username2":"y-points",
    "username3":"z-points",
}
```

This endpoint awards a point to a user

### HTTP Request

`GET <BaseEnpoint>/user/<username>`

## Show User Info

```shell
curl base_url/users/<username> -X GET
```

> The above command returns JSON structured like this:

```json
{
    "total_score" : 738, \\ The Global Score total
    "community_wise": {    \\ The Global Scores for all the communities they have been or are a part of
        "community_name1": 32,
        "community_name2": 47,
        "community_name3": 58,
    }
}
```

This endpoint shows user info.

### HTTP Request

`GET <BaseEnpoint>/user/<username>`
