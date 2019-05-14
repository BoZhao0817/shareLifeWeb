# ShareLife (house exchanging website)

## Introduction:
The website is called “Sharelife”, the purpose of this website is to provide a platform for users to exchange their houses without using money. people can post their home, search for a destination accommodation, chat with like-minded people. The idea comes from real-life scenario that when holidays or vacations come, travelers leave their home empty, and pay for accommodation, such as Airbnb or hotel, in their destination place. Then an idea just comes to me that why can’t people exchange their homes with others who want to travel to their place. 
For example, if people in Urbana-Champaign want to go to Chicago for travel, and at the same time, people in Chicago also want to go to Urbana-Champaign, then they can exchange their apartment. Specifically, when people make their holiday plans, they can come to this website and find someone who also wants to travel to their base cities, then the two groups exchange their homes and set foot on the journey with excitement, but without paying anything.

## Data: 
The data is from Airbnb, it’s all real data, downloaded from insideairbnb, then imported to the database. 700 real data in-total around 7 major US cities including NYC, LA, Chicago, etc., are collected to empower the project. Then 667 valid data are imported into the database.


## Database functionality:
The website has four administrators: bo, tester, tester1, and yangyang.
The password of the first three is “(secret)”, the last one is “123456”. 
Every user can post, edit and delete his or her own post, and the main difference between users and administrators is the administrator could use admin page.
<br><br>
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture1.png)
Here’s the structure of the website. Main tables are posts, post_details, users and location.
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture2.png)
 


### Functions
* Smart Search<br>
Search for places at a given destination is a crucial function for the website. the search function shows result beyond users’ restrictions and also visualized the search result. Specifically, the search system not only tells user which posts fit exactly with user’s requirement, it also shows some post which satisfies most requirements.  Also, the website provides a visualization for the searched results and use different markers indicating the level of matching in Google Map. 

* Chat System<br>
The website provide a chat system for private conversations. 


## Demo 
The password of the administrator is “(secret)”
<br> User id: tester          password: (secret)<br>

The password for all the other users is “123456”
<br>User id: Sharon and robert94670          password: (secret)<br>

1. login and add a post
Login with the userid: bo, when user login, they will jump into the index page, here’s the user’s post. Now add one post by click morepost.
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture3.png)
  
Here we go to the “add” page.<br>
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture4.png)

<br>
After adding a new post, this user’s post will show. Then this user can edit and delete the post.
Below this part, are other user’s posts.


2. explore other users’ posts.<br>
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture6.png)
Here are all the posts, users can click the picture or the title to jump into the post detail page.
<br>

3. post detail page<br>
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture7.png)
<br>Post detail page shows all the information about the house, including the date and facilities, these are all real data.
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture8.png)


4. chat room
In the detail page, there’s a chatroom for users to chat with each other. When you leave some messages here, the messages will be showed in the chatroom. But there’s one bug here, you have to right click “chat with XXX”, then you could jump into the chatroom page.
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture9.png)
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture10.png)
<br>
   
Here is the chatroom page<br>
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture11.png) 

For this example, we use userid: yangyang to leave a message, then the post owner: Reem63208 will see messages at the post detail page. Then when user Reem63208 click reply, he will jump into the chatroom, and see the messages before.<br>
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture12.png)
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture13.png)
<br>
    
5. search function
Users can use the search function to find their ideal place<br>
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture14.png)
Here is the search result, list all the houses that matches the user’s interest.<br>
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture15.png)
<br>

And here is a data visualization part:<br>
![imge](https://github.com/BoZhao0817/shareLifeWeb/blob/master/Picture16.png)

