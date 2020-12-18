# Waterbuffalo Micromanagement: An Unusual Organisational Application

![alt text](https://github.com/waterbuffalo13/Waterbuffalo-Micromanagement/blob/master/screenshot-gif.gif)

# The Vision

>"Achievement of your happiness is the only moral purpose of your life, and that happiness, not pain or mindless self-indulgence is the proof of your moral integrity, since it is the proof and the result of your loyalty to the achievement of your values" - Ayn Rand

I have a hunch that people rely too much on "gut feeling" to justify how they spend their time. This methodology is flawed because of the limitations of individual human knowledge and the cognitive biases towards familiarity and self-indulgence. What activities does a perfect schedule consist of, truly? The single *best* schedule out of all the possible configurations of schedules and how much different is it from the one I am currently experiencing? Where every activity is micromanaged for the sole purpose of maximising for the single factor of wellbeing? And what if I could draw from the collective experience of large groups to form the basis of answering this question? We as humans never consider the humongous build-up of opportunity cost and the waste of potential that happens when an entire civilisation chooses to lives by an inefficient methodology.

The purpose of this application is to view life as an optimisation problem and to apply techniques from data science to the study of wellbeing in the form of a usable web app. This can be achieved by making data-driven calculations on schedules and events to assess their quantitative impact on "wellbeing". In this way the app can make recommendations on what to do and how to act, and work towards predicting and avoiding negative outcomes. 

# The Approach 

I'm building an application that exists in the form of a multi-functional organisational and planning web-app that provides value by providing the following tools:
- Sequential to-do list: Set out some goals for the day and tick them off as you .
- Habit-Tracking: You want a six-pack? That's cool mayn! How much do you bench? What?! What do you mean you don't go to the gym?
- Scheduler: Plan out your day and see visually how you are spending it. Also do fancy things like generate suggested schedules.
- Journal: Record important events or achievements. Write and save notes about your day or any thoughts you have and view them at any time.
- Mood-tracker: How does your mood fluctuate throughout your day and what should you avoid/do more.
- Diet Planner: Keep track of your calories. Useful for people trying to lose/gain weight or be healthier.

Advanced
- Tree-based Planner: (inspired from Roberto's Satplanner (https://www.kickstarter.com/projects/lucenera/satplanner/description). Maybe even create recommended plans for days. Good for planning multiple outcomes (promotions/redundancies, divorce/marriage, kids/no-kids, employment/unemployment etc )
- Financial Planning: I really want to buy a house but when will I be able to based on my current finances? What if I make adjustments? Maybe I'm overdue for a holiday? Can I afford it?
- Health & Fitness Planning: Would you like to know when exactly you'd get that six-pack/run a marathon/lift your bodyweight? even if sedentary stil useful.
- Recommendation: Feeling bored? Here are some interesting activities that you might like! Feeling anxious? Tell me about it on this page. Feeling the existential angst? Hey I've booked a holiday for you and the family in Switzerland. No need to thank me man. And great work on that presentation you did at work! It was awesome!

I also placed special attention to the look and feel of the application. After all, what good is an application if nobody wants to use it? And these applets are interconnected with analytics to produce useful statistics about the end-user. 

I want to explore systematic strategies to allocate uncommitted time in a way that maximises individual human happiness over the lifespan by tracking and optimising for a wellbeing index. The ultimate goal is help the user make progress towards a state of "perfect resource allocation"; a hypothetical psuedo-mystical pattern of behaviour where a person is doing precisely what they need to all the time. The concept of time is viewed as finite resource that is continuously being exchanged for activities that provides some form of value. This project views life as a series of these (time-> activity-> value) transactions. By viewing life from this perspective, concepts such as return-on-investment and opportunity cost become quantifiable and measurable.

I place a strong a emphasis on concept on continual exploration and consistent self refinement of values.

This project itself exists in the form of a useful organisational and planning tool that contains a useful suite of applets such as todo lists, schedules, habit trackers, diet planners and journals. I also placed special attention to the look and feel of the application. After all, what good is an application if nobody wants to use it? And these applets are interconnected with analytics to produce useful statistics about the end-user. 

I believe that there is great potential for the usage of collective data gathering to empower individual self-improvement (in a future build this will allow multiple users), and the development of AI for the optimisation of daily schedules.  I want this data analytical tool for self-improvement to deliver real value to people with the same very peculiar desires that I have i.e. to see my personal statistics laid out in front of me and to make better decisions.

Want to work with me, or learn about the project? Feel free to hit me up on waterbuffalo13@tutanota.com


## Phase 1: Prelim Database
![alt text](https://github.com/waterbuffalo13/Waterbuffalo-Micromanagement/blob/master/misc_image/er_diagram.png)

## Why should I use this app?

You will get (now or eventually) access to the following features:
- Sequential to-do list: Set out some goals for the day and tick them off as you .
- Habit-Tracking: You want a six-pack? That's cool mayn! How much do you bench? What?! What do you mean you don't go to the gym?
- Scheduler: Plan out your day and see visually how you are spending it. Also generate suggested schedules.
- Journal: Record important events or achievements. Write and save notes about your day or any thoughts you have and view them at any time.
- Mood-tracker: How does your mood fluctuate throughout your day and what should you avoid/do more.
- Diet Planner: Keep track of your calories. Useful for people trying to lose/gain weight or be healthier.

Advanced
- Tree-based Planner: (inspired from Roberto's Satplanner (https://www.kickstarter.com/projects/lucenera/satplanner/description). Maybe even create recommended plans for days. Good for planning multiple outcomes (promotions/redundancies, divorce/marriage, kids/no-kids, employment/unemployment etc )
- Financial Planning: I really want to buy a house but when will I be able to based on my current finances? What if I make adjustments? Maybe I'm overdue for a holiday? Can I afford it?
- Health & Fitness Planning: Would you like to know when exactly you'd get that six-pack/run a marathon/lift your bodyweight? even if sedentary stil useful.
- Recommendation: Feeling bored? Here are some interesting activities that you might like! Feeling anxious? Tell me about it on this page. Feeling the existential angst? Hey I've booked a holiday for you and the family in Switzerland. No need to thank me man. And great work on that presentation you did at work! It was awesome!

This is a WIP. 

## Why build this app?

After having more then a few bad days in a row, I had lured into a state of existential anxiety. I spent a lot of time thinking about how it would be like under different circumstances. What if I had made different choices on what people I met, things I had done, subjects that I studied, risks I had taken? At one point I tried to draw a tree-like graph of all the different possibilities but I couldn't produce anything meaningful. And even if I did, it wouldn't really matter because I can't go back in time and evaluate all my alternatives. I think I wanted to build a fully rational, impartial advisor that would help me understand who I am and who I could trust to guide my trajectory through my life in a way that was reliable. 

## How do you even quantify wellbeing?

The same way inflation, socio-economic development and various other phenomena is measured i.e. through an index. A collection of non-related factors. With this index it is a little tricky as you can't use the same coefficients as priorities vary from person to person. Coming up with a concise formula that describes the relationship between activities and events and mood is a tricky business. Whilst I wait for future patrick to make sense of it, I just get the user to use a number between -3 (sucidal) and 3 (euphoric) based on how they feel that I input along with the activities that populates the mood graphs. 

## What strategies do you use?

I haven't implemented any yet! Since this entire project was inspired by trading algorithms (now does this all make sense?!) it's likely many of the same approaches used in traditional finance portfolio optimisation can be applied to this context. I'm more of an AI enthusiast than an expert but I hope my knowledge grows with time. My priority right now is to develop the infrastructure so that it can support all the analysis I have planned.

## How does the virtue system work?

The virtue system is a series of meta-data collected that reflect a given ideal. Productivity is what proportion of time you spend on high-quality activities. Integrity is what proportion of goals/commitments you actually follow through on. Self-restraint is how well you adhere to a system of positive habits. Wisdom represents time allocated to self-mastery. And rationality is simply the weighted average of all the previous. Fundamentally the idea is to give people a reason to use the application without trying to "win" it. These values reset every week, and so you always have a fresh start to go above and beyond.

## The End Goal: A Collective Conciousness?

My goal is to support the end users and to produce lasting value. To enrich peoples lives with new hobbies, lifestyles and ways of overcoming problems that they had not  previously considered. To answer definitively if your goal should be to work compulsively with the promise of a luxurious lifestyle, or to laze around on a field in a developing country,  or to tour the world in a van like some dried-up hippy. To understand how other users have gotten there and to provide the tools to get there. To reinforce good habits and promote good behaviour. To promote efficient resource-usage (e.g. time, money etc) and to spend it in ways you had not previously considered. To work to solve deeply embedded problems like mental health, debt and bad behaviour through multiple behavioural streams. To act as a companion in times of great difficulty and to provide fresh, new perspectives and call to actions. To increase collective commitment to rational self-interest.


>Who am I and what do I want? And given all the uncertainity that is inherent in life how should I act? With what goal? And how can I navigate all the decisions yet to come? How does the life I want even look like? And how do I get there? Is it possible to systematise a life strategy? To understand and realize potential and overcome the tragedy of opportunity cost? 
s, and to make recommendations on how to live that avoids short-term, idealistic or emotional reasoning

