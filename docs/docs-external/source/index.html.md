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
Rep Sys is a reputation system for collaborative developer groups that build and ship software together on the internet. The goal of the reputation system is to define clear levels of experience, foster collaborative learning, and increase trust among strangers. 

# Levels
A level describes the impact/contributions that a developer has demonstrated on their software projects. 

## Software
**S59** - New to writing software - does very little to no work independently and requires substantial guidance when working on a software project. Unfamiliar with tools/processes required to collaborate on group software.

**S60** - Familiar with writing software - e.g. writes working code. Works independently while requiring some guidance when implementing features, debugging, or resolving general issues. Familiar with tools/processes required to collaborate on group software.

**S61** - Comfortable writing software. Acts as a guide/mentor to developers on their team. Writes working and well tested code. Works independently with little to no guidance when implementing features, debugging, or resolving general issues. Comfortable with tools/processes required to collaborate on group software.

**S62** - Comfortable writing software and architecting software systems. Acts as a guide/mentor to developers on their team. Writes working and well tested code. Works independently with little to no guidance when implementing features, architecting systems, debugging, or resolving general issues. Comfortable with tools/processes required to collaborate on group software.

**S63** - Experienced writing software and architecting software systems. Acts as a guide/mentor to developers on their team. Writing working and well tested code isn't enough - values thoughtful software design and makes a concious effort to write clean code. Capable of architecting reliable, highly available, fault tolerant software systems comprising of multiple components and has a deep understanding of going from concept to a deployable production system. Works independently with little to no guidance when implementing features, architecting systems, debugging, or resolving general issues. 

**S64** - Experienced writing software, architecting software systems, and leading a team of developers to build and ship software. Acts as a guide/mentor to developers on their team. Beyond writing great software - elevates their team members and holds them accountable to the software they build and ship. Beyond architecting great software systems - guides their team through technical complexity and architectural discussions where necessary. Capable of architecting a software system comprising of multiple components and has a deep understanding of going from concept to a deployable production system that can scale to millions of users. Works independently with little to no guidance when implementing features, architecting systems, debugging, or resolving general issues. 

**S65** - Experienced writing software, architecting software systems, and leading multiple teams of developers to build and ship software. Acts as a guide/mentor to developers on their team. Beyond writing great software - elevates their team members and holds them accountable to the software they build and ship. Beyond architecting great software systems - guides their team through technical complexity and architectural discussions where necessary. Capable of architecting a software system comprising of multiple components and has a deep understanding of going from concept to a deployable production system that can scale to millions of users. Works independently with little to no guidance when implementing features, architecting systems, debugging, or resolving general issues. 

# Apps
## Reddit

Integrating into a Reddit community is easy...(to be updated)

## Discord

Integrating into a Discord community is easy...(to be updated)

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
