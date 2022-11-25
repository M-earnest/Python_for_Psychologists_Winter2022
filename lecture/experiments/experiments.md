# Running experiments in Python

After spending quite a good while on important prerequisites concerning scientific computing and the basics of the `python` programming language, it's finally time to combine them via transitioning to more applied topics. This adventure will start with a brief exploration of how to create and run experiments using [PsychoPy](https://www.psychopy.org/index.html), a `python library` dedicated to conducting experiments in the realm of `psychology` and adjacent fields. Due to time constraints we will only have a quick look at things and showcase the most important aspects to allow folks to explore things further after the course ends. We'll further concentrate on using psychopy to further your understanding of the Python essential such as control-flow statements.

## Topics 💡👨🏻‍🏫 

In the following you'll find the `objectives` and `materials` for each of the topics we'll discuss during this session.


### Introduction to PsychoPy - I

Most of us already conducted or at watched or help conduct an experiment. However, there's a fair number of different software options and tools out there, which mostly depends on the computational infrastructure at hand, but also on what people have the experience and skills to master. 

That being said: We'll quickly discuss some tools to conduct experiments and work out if we can actually use `python` based resources in this context with a clear conscience or if you're better off by defaulting to paid software packages.

To get some idea on how to present experiments via Python, we will explore the `python library` [PsychoPy](), including its setup, basic working principles, as well as advantages and disadvantages, showcased on a very simple experiment. Buckle up y'all, this is the first time we will use `python` "in the wild".      

#### Objectives 📍

- running `experiments` using `python`
    - Exploring `PsychoPy`
    - basic setup & interaction
    - experiments, trials, stimuli, responses
    - a very simple experiment
- Ask and answer questions
- Have a great time

#### Materials 📓

There are three different sets of materials for this topic. A `slides`, a `jupyter notebook`, as well as several `python scripts` (.py) which can be run using `Psychopy`.

You can find the `slides` here:
<iframe src="https://docs.google.com/presentation/d/1zzvIqxXAqJ-ax77gxyZ3_oiCnaJYliZUIwP23OOjOMM/edit#slide=id.g108e193bf9d_0_111" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

We've also got the recap on the last Python lesson here:
<iframe src="https://docs.google.com/presentation/d/1V_Ww6gECVAXPgR9MktS5e_OnGq8_44DkyOfnI-ejAeo/edit?usp=sharing" frameborder="0" width="960" height="700" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>


And the `jupyter notebook` which contains a condensed version of the `slides` in the `ToC` on the left via
[Experimentation - Introduction to PsychoPy](https://m-earnest.github.io/Python_for_Psychologists_Winter2022/experiments/intro_psychopy_I.html) .

To get the discussed Python scripts you can either download the [course content](https://github.com/M-earnest/Python_for_Psychologists_Winter2022/archive/refs/heads/main.zip) again and replace the old "experiments" folder with the new one provided or you can download the python scripts directly by opening the respective python file in the [github erpository](https://github.com/M-earnest/Python_for_Psychologists_Winter2022), click `'Raw'` and save the file locally via `ctrl/cmd + s`.


### Homework assignment #6
Your sixth and last homework assignment will entail the generation of a “new” psychopy experiment

You are free to copy any of the existing experiments, but at least change the instruction, stimuli and file/experiment name. You'll get full marks, if the experiment runs without crashes, collects participant input in a gui dialogue, logs responses and outputs a .csv file which contains the collected data.
Bonus: Use a different stimulus modality

Save it as a .py file and e-mail it to ernst@psych.uni-frankfurt.de

**Deadline: 23/12/2023, 11:59 PM EST**


### optional/reading/further materials

Here are some cool videos providing some further insights into the world and capabilities of `PsychoPy`.

First, a nice tutorial on how to create a “`line bisection task`” using `PsychoPy`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dQSL_ogaLG8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Want to know how far you can go with `PsychoPy`? How about coding an entire video game? Yeah, that's possible!

<iframe width="560" height="315" src="https://www.youtube.com/embed/ISHAnDF4Xkc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

As we couldn't address a lot of things, check out this great in-depth dive into Psychopy itself:

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=GSv60zgQlB8&list=PL6PJquR5BWXllUt585cRJWcRTly55iXTm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

