**Preface by Bart Veldhuizen:**

It must have been sometime in 1998 when I first downloaded a copy of a strange and unknown 3D application called Blender. It wasn't a particularly good experience - it didn't look like anything I had ever seen, there was no documentation available at all, and there was no way to get in touch with other users. I got in touch with Ton Roosendaal and in the years that followed, I wrote tutorials, worked for Ton at his company Not a Number and founded BlenderNation - still the main news site for Blender.

During that time, what has fascinated me most was the Blender community - a world-wide loose band of artists, teachers, software developers and 3D lovers in general. All of them attracted by the notion of this high-quality, powerful, open-source, free 3D package.

Unlike the communities of many similar but closed applications, the people in this community tend to be very open to each other as well: ask a question and you will receive an answer. Mention a bug in the software and someone may fix it for you before the day is over. Ask to become involved and we will find a place for you. And this generosity is not limited to the hobbyist users - it extends to the many professionals as well.

And professionals they are - especially during the last few years Blender is gaining popularity fast in environments like movie studios, special effects companies, advertising agencies and schools. The community is rife with examples of their outstanding work, which in turn convinces more people of Blender's qualities.

The fact that Blender has a built-in game engine (or rather: a fully embedded interactive environment) is one of its lesser-known features. But like the other aspects of the software, it has seen a huge leap in quality: it now has a very capable scripting environment, GLSL rendering, and node-based materials. It is an extremely useful tool not just for making games, but for creating interactive simulations of any kind.

Seeing people like Dalai and Mike invest their time in the huge undertaking of writing a book about the Blender Game Engine gives me courage that it will earn the popularity it deserves.


Bart Veldhuizen


**About Bart Veldhuizen**

Bart is a long-time Blender evangelist who has actively participated in the education and dissemination of Blender. He is known for his work as community manager for Blender before it was even open source. More recently, Bart founded BlenderNation and BlenderNetwork, two of the central hubs for Blender users around the world.

---

**Dedication**

To my niece for being such a special little princess.

-- Dalai

To my mom and dad, who have done everything for me.

-- Mike

---

**Acknowledgement**

The driving force of an open source project is its user community. We want to start by thanking the overall support you have shown for Blender and specifically for this book.

We would also like to thank the Blender Foundation, and its chairman, Ton Roosendaal, for facilitating the development of this amazing software, Blender. We are grateful for an remarkable team of developers who have tirelessly worked to improve the Blender game engine: Benoit Bolsee, Brecht van Lommel, Campbell Barton, Daniel Stokes, Mitchell Stokes, and many others.

From the vast Blender community we would like to thank two people in particular. Yorik van Havre for helping peer reviewing half the book and providing valuable feedback. Stephen Danic for bringing the embryonic project of this book and entrusting that to us, resulting in what you have in your hands.

Lastly, our deepest appreciation goes to our families and friends who supported us on this journey.

**Introduction**

There is an old Chinese proverb that says:

&quot;When you plan for a year, sow rice.

When you plan for a decade, plant trees.

When you plan for a lifetime, educate people.&quot;

In this always changing technology-driven world, one can&#39;t plan further than five years ahead. Maybe we were better off farming rice instead of writing this book. Nevertheless, we feel the duty to pass along the torch of all the knowledge we have been so gently taught.

And here it is: this book is the result of two long-time Blender users and friends wanting to share what they know about the game engine. **Dalai Felinto** , an active developer of Blender, will offer insights into the game engine from the unique perspective of a coder. While **Mike Pan** , a long time Blender artist, will approach Blender from more of a practical perspective.

When both of us started, there wasn&#39;t much material out there for teaching the way into the Blender game engine. This is getting better over time, but we still believe there was a gap from the available material and the current needs of the professional market.

We hope this work can be well received and help to pave the way to a new era of creative interactive projects with the game engine.

**What You&#39;ll Find in This Book**

**Chapter 1** starts off by giving you a brief introduction to 3D computer graphics as well as Blender in general. This serves as a foundation for the rest of the book. If you haven&#39;t used Blender before, there should be sufficient information in this chapter to get you familiar with the terminology and interface.

**Chapter 2** is written in a do-as-I-say-and-don&#39;t-ask-questions style. You will follow a lengthy tutorial to create a small but complete game. This might actually be the most demanding chapter in the book if you haven&#39;t used Blender before. If you are discouraged, don&#39;t be. It only gets easier from here.

The bulk of the book is organized into chapters, each focusing on a single component relevant to the game creation process: **chapter 3** , Logic Bricks, **chapter 4,** Animation, **chapter 5** , Graphics, **chapter 6** , Physics, and **chapter 7** , Scripting. These chapters are made to be as independent as possible, but since the game engine is a system, sometimes it is difficult to talk about certain features in isolation.

**Chapter 8** talks about polishing and optimization. At this point, you should have a pretty good idea of how the game engine works. This chapter will expand that knowledge by talking about the game creation process as a whole.

**Chapter 9** deals with the final milestone before your work is seen by everyone: the technical aspects of packaging and releasing a game created with Blender.

**Chapter 10** contains a selection of games people have made using the Blender game engine. The aim is to give you a glimpse at the possibilities of Blender.

The aim of the book is not only to teach the game engine, as that would make this a software manual. We not only want this book to teach but also to share our experiences of using Blender by giving you tips, hints, and workarounds to common problems and questions.



**Who This Book Is For**

This book is designed for anyone who has an interest in using the Blender game engine to make games. While having some Blender experience is ideal, we tried really hard to make sure the book is accessible for everybody. The book works best when you have access to a computer (with Blender installed) at the same time, as this isn&#39;t a book that you can just read from cover to cover on the beach.

As this is a book about the Blender game engine, topics such as advanced modeling and animation techniques are beyond the scope of this book. If you are looking for a book that teaches you how to move your character in a game, welcome!  If you are looking for a book that teaches you how to animate your characters so that they walk realistically, numerous other books are better suited to that task. Likewise, Python programming in Blender will also be taught without assuming any prior Python knowledge; but this book is not a replacement for a full-fledged Python manual.

This book is written for Blender version 2.66. Any of the other Blender 2.6x releases should also be compatible with the book, but expect minor changes as the version of Blender you use deviate from our target version number.

