# Database Design
[TOC]

## Database Type 
PostgreSQL

## Tables
### Tribe
|name|field|description|
|---|---|---|
|Id|Guid|primary key|
|Name|VarChar(50)|name|

### User
|name|field|description|
|---|---|---|
|Id|Guid|primary key|
|Username|VarChar(50)|username|
|PasswordHash|???|hash code for users password (we dont want to store their password directly for security reasons)|
|PosterId|Guid|reference Id for posts made by this user| 
|Title|VARCHAR(50)|title of the user|

### Boadcaster 
|name|field|description|
|---|---|---|
|Id|Guid|primary key|
|name|VarChar(50)|name|
|PosterId|Guid|reference Id for posts made by this user|


### Thread
|name|field|description|
|---|---|---|
|Id|Guid|primary key|
|PosterId|Guid|reference Id for posts made by this user|

### Comment
|name|field|description|
|---|---|---|
|Id|Guid|primary key|
|ThreadId|FK to Thread Id| reference to Id of thread this comment is in|
|ParentId|FK to Id of parent comment or Null|referene to parent comment|

### Trinkit
|name|field|description|
|---|---|---|
||

## Table Map
```puml
testdot
```