# PhysioClinic

![screenshot of Responsive Image](readme/docs/images/responsive_image.png)

View the live site [here](https://physio-clinic-heroku.herokuapp.com/)


# Table of Contents

1. [User Experience (UX)](#ux)<br>
    i.  [Strategy](#strategy)<br>
    ii. [Scope](#scope)<br>
    iii. [Structure](#Structure)<br>
    iv. [Skeleton and technical design](#skeleton)<br>
    v. [Surface](#surface)<br>
      
2. [Features](#features)<br>
    i. [Current Features](#features-existing)<br>
    ii. [Features to implement](#features-toimplement)<br>

3. [Testing](#testing)<br>

    i. [User Stories/feature testing](#user-stories-testing)<br>
    ii.  [Automated testing](#automated-testing)<br>
    iii.  [Known issues during development and testing](#known-issues)<br>
    iv. [Validation testing  ](#validation-testing)<br>
    v. [Javascript testing](#js-testing)<br>
    vi. [Unfixed bugs](#unfixed-bugs)<br>
4. [Deployment](#deployment)<br>
5. [Technologies Used](#technology-used)<br>
6. [Credits](#credits)<br>
7. [Acknowledgements](#acknowledgements)<br>


## Introduction
**The project concept**

PhysioClinic is the webpage for a fictional Physiotherapy Clinic. 
On this webpage the Owners share information about various kinds of treatments on offer. 
Due to ever-enhancing skills of the Clinic's staff, new staff members joining the Clinic and changing trends among Clients, Staff members have the ability to add, edit and delete cards containing descriptions of treatments. 
Client users of this service can read descriptions and express their attitudes about specific treatments through likes and comments. They may also book treatments and contact the Clinic for general queries.

# 1. User Experience (UX) <a name="ux"></a> 
### **Project goals**
The main goal of the project is to provide a platform for engaging prospective and current clients interested in using PhysioClinic's offering for enhancing the state of their health. This should be achieved through several sub-goals:
- To enable staff users to post, edit, read and delete content related to company's offering.
- To enable registered users to comment and like specific treatments and read other users' input.
- To enable all users to read about company's offering and see other users' reviews, comments and likes.
- To enable registered users contact the company to book specific treatments.
- To enable all users to contact the company for any reason.

### **Site owner goals**
- To ensure the company's up-to-date offering is broadcast in a timely and efficient manner.
- To increase prospective and current users' interest in the offering and to promote sales through encouraging engagement within the community.
- To maximise customers' retainment.
- To promote knowledge on benefits of treatments on offer.
- To receive requests for booking.
- To enable custommer - company correspondence.
- To build customer database.
- To differenciate between different kinds of users in terms of access and ability to edit and delete information.
- To assure access to the service on different kinds of devices.

### **User goals**
- To be able to use service intuitively and with ease.
- To be able to read content withouth sharing any details.
- To find details on what kinds of treatments are offered and about their benefits.
- To be able to contact the company to book a specific treatment or about other related topics.
- To open and then access account for easier communication.
- To log in and log out as needed.
- To log in with a chosen user name to maintain privacy.
- To have an esthetically pleasing and functionally easy experience while using the webpage.
- To be able give feedback on treatments already received.
- To be able to upload, update and delete information on treatments contained in the posts (for staff users only).

## i. Strategy <a name='strategy'></a>

## User stories

### **1. Epic: Account management**

1.1 As a **site user** I can **access site without logging in** so that I can **read information about available treatments**.

1.2 As a **site user** I can **register** so that **I have access to personalized service**.

1.3 As a **site user** I can **log in using my username and password** so that I can **access site's enhanced functionality**.

1.4 As a **site user** I can **log out of my account** so that I know **my information stays confidential**.

1.5 As a **site user** I can **see at all times my current login status** so that **I know I'm in control of access to my enhanced service on currently used device**.

1.6 As a **site user** I receive **confirmation of logging in and logging out visible on webpage** so that I **instantly know if the operation was successful**.

1.7 As a **staff site user** I can **access enhanced functionality** so that I can **add, edit and delete content on webpage**.

### **2. Epic: Navigation**

2.1 As a **site user** I can **navigate the service intuitively** so that I can **utilize all of its content**.

2.2 As a **site user** I can easily **browse through available treatments** so I can **decide which ones are most appropriate to me**. 

2.3 As a **site user** I can **navigate the site on all kinds of devices** so that **I am not limited to any kind of device**.

### **3. Epic: Customer engagement**

3.1 As a **site user** I can **read and respond to available content** so **my experience on the site feels engaging and interactive**. 

3.2 As a **site user** I can **engage in activities that other users can also participate in** so I can **feel part of a wider community**.

3.3 As a **site user** I can **locate company's social media accounts** so I can **stay in contact through alternative means**.

3.4 As a **site user** I can **use the website for communication with the company** so that I can **send general queries or request booking for a specific treatment**.

3.5 As a **registered site user** I can **use website for communication without having to reenter my details** so that **sending my message requires minimum efford from my side**.

3.6 As a **site owner** I can **control content showing on the website** so that **the whole website content is in line with company values and supports its mission**.

### **4. Epic: Company offer**

4.1 As a **site user** I can **quickly get a general idea about services on offer** so that I can **prioritize which content to read more thoroughly**.

4.2 As a **site user** I can **read thoroughly about chosen treatments** so that I can **read content most appropriate to my needs**.

4.3 As a **site user** I can **respond to content via likes and comments** for **increased sense of community** (registered users only).

4.4 As a **site user** I can **take part in polls and see poll results** so I can **feel more engaged with the company and the health-oriented community**.

4.5 As a **staff site user** I can **create, update and delete polls** so that **polls as means of engaging users and gathering information are used according to their purpose**.

4.6 As a **site owner** I can **easily activate and deactivate content is visible to the public**.

4.7 As a **site owner** I can **prioritize which treatments are showing first on the site** so that I can **influence demand on offering of my choice**. 

### **5. Epic: Site admin**

5.1 As a **site admin** I can **create, update and delete user profiles in admin page** so that **all users have appropriate access to site services**. 

5.2 As a **site admin** I can **create, update and delete posts and comments in admin page** so I can assure that **only content in line with company's ethos and goals is made available**.

5.3 As a **site admin** I can **create, update and delete polls** so that **polls as means of engaging users and gathering information are used according to their purpose**.

5.4 As a **site admin** I can **read, update and delete booking requests** so that **booking requests are dealt with**. 

