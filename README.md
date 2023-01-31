# DECO Profiles
#### Video Demo:  https://www.youtube.com/watch?v=bgoYd58DNDQ

<img src="https://github.com/giopolykra/Deco_Profiles/blob/main/photo.png" width="2500">


#### Background

In scubadiving where breathing gasses are used at ambient pressure greater than the surface atmospheric pressure, divers are in need of planning and monitoring their dive profile using algorithms and tables in order to avoid decompression sickness (DCS) which is the result of excess dissolved innert gas in muscle tissues that expands from a solution into bubbles as they ascend can cause.

Bühlmann decompression algorithm is an inverse exponential model that separates the tissues in the body into N different compartments each having a different saturation half time. As the diver descents into the water collumn or spends time at depth he is in-gassing, meaning his tissues are loading with innert gases like Nitrogen and or Helium each having a different half time for each of the tissue compartments.

The tissues with the smaller half time dictate the dive profile of shallow dives while the tissues with longer have time dictate the longer and deeper dives.

As more innert gas is disolved into the tissues the depth the diver can ascent to with safety without running into the risk of DCS, called critical ceiling is dicreasing. Thus the diver at his way back to the surface has to ascent at a slower rate and/or perform stops at certain depths in order to off-gas safely.

Let's now move on to the project's code!

### Description:

This web-based application lets you calculate a dive plan (proposes breathing gases and schedules decompression stops) given certain parameters that the user provides. It also calculates the Maximum Operating Depth (MOD) of a breathing mix containing a certain percentange of oxygen resulting in a certain partial pressure of oxygen at that depth (ppO2), both set by the user.


### MOD

Iside the templates folder there is a file called mod.html. In this site, in the left table, the user can compute the maximum operating depth (MOD) he can dive, given a certain partial pressure of oxygen in the breathin mix. Above a certain threshold (ppO2=1.6) the breathing gas becomes toxic, having dengerous side effects to the neural system. The diver has to select a conservative choice for the ppO2 for his breathing mix and then see what is the maximum depth he can safely go to.

In the right side of the page there is a table


### Running

Start Flask's built-in web server (within `project/`):

```
$ flask run
```

Visit the URL outputted by `flask` to see the distribution code in action. You will be able to log in or register in order to access the website.

### Understanding


#### `app.py`

Open up `app.py`. Atop the file are a bunch of imports, among them CS50's SQL module and a few helper functions. More on those soon.

After configuring [Flask](http://flask.pocoo.org/), notice how this file disables caching of responses (provided you're in debugging mode, which you are by default in your code50 codespace), lest you make a change to some file but your browser not notice. Notice next how it configures [Jinja](http://jinja.pocoo.org/) with a custom "filter," `usd`, a function (defined in `helpers.py`) that will make it easier to format values as US dollars (USD). It then further configures Flask to store [sessions](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions) on the local filesystem (i.e., disk) as opposed to storing them inside of (digitally signed) cookies, which is Flask's default. The file then configures CS50's SQL module to use `finance.db`.

Thereafter are a whole bunch of routes, only two of which are fully implemented: `login` and `logout`. Read through the implementation of `login` first. Notice how it uses `db.execute` (from CS50's library) to query `finance.db`. And notice how it uses `check_password_hash` to compare hashes of users' passwords. Also notice how `login` "remembers" that a user is logged in by storing his or her `user_id`, an INTEGER, in `session`. That way, any of this file's routes can check which user, if any, is logged in. Finally, notice how once the user has successfully logged in, `login` will redirect to `"/"`, taking the user to their home page.  Meanwhile, notice how `logout` simply clears `session`, effectively logging a user out.

Notice how most routes are "decorated" with `@login_required` (a function defined in `helpers.py` too). That decorator ensures that, if a user tries to visit any of those routes, he or she will first be redirected to `login` so as to log in.

Notice too how most routes support GET and POST. Even so, most of them (for now!) simply return an "apology," since they're not yet implemented.


#### 'helpers.py'

Inspired by the finance problem I am using the same appology function that rederes the template `apology.html` as well as the  `login_required` function.


#### project.db

Similarly to the finance problem, in this file I store informations using SQL about the registered users and their passwords.

#### `requirements.txt`

The `requirements.txt` file simply prescribes the packages on which this app will depend. What is different from the finance problem is that here I require the Plotly package.

#### `static/`

Glance too at `static/`, inside of which is `styles.css`. That's where some initial CSS lives. You're welcome to alter it as you see fit.

#### `templates/`

Now look in `templates/`. In `login.html` is, essentially, just an HTML form, stylized with [Bootstrap](http://getbootstrap.com/). In `apology.html`, meanwhile, is a template for an apology. Recall that `apology` in `helpers.py` took two arguments: `message`, which was passed to `render_template` as the value of `bottom`, and, optionally, `code`, which was passed to `render_template` as the value of `top`. Notice in `apology.html` how those values are ultimately used! And [here's why](https://github.com/jacebrowning/memegen) 0:-)

Last up is `layout.html`. It's a bit bigger than usual, but that's mostly because it comes with a fancy, mobile-friendly "navbar" (navigation bar), also based on Bootstrap. Notice how it defines a block, `main`, inside of which templates (including `apology.html` and `login.html`) shall go. It also includes support for Flask's [message flashing](https://flask.palletsprojects.com/en/1.1.x/quickstart/#message-flashing) so that you can relay messages from one route to another for the user to see.


### index.html

Iside the folder templates there is a file called index.html. Here I have implemented the code for the main page in html and javascript functions.
I have a first row where the user can input various parameters (in the Metric system) for the dive he wants to do, like the altitude, depth, bottom time, the percentage of the oxigen and helium in the breathing mix, the descent and ascent rate or the surface breathing rate of the individual. The user can also choose between different versions of the decompression parameters algorithm (such as ZHL16c/ZHL16b/ZHL16a), which basically changes the half times of each gas for each tissue compartment.

When the user imputs the depth, he gets an automatic proposal for appropriate breathing standar gas at descent. I have not yet implemented a gas switch at descent which a diver has to do in order to avoid breathing the wrong gas at the wrong depth. In a later version I will add this functionality.

When the user provides the above inputs, a plot showing the  dive plan is rendered at the bottom right of the page with information about the depth and the time at the two axes. On the bottom left a table with the decompression stops in meters and the corresponding times in minutes is also shown.

If the dive is deep or long enough the middle left table will also show the proposed decompression gas mixes that the diver has to use at certain depths  in order to de-gas quicker and increase his critical ceiling in order to reach the surface. In a later version I will let the user have the freedom to choose his desirable decompression gas which will alter the dive plan and the duration of the decompression stops anew.

Finally in the middle right table I also output the total volume of breathing gas needed in order to achieve the dive. I also translate it in the number of aluminum tanks needed and the filling pressure they have to be in. The user can choose the conservatism (safety backup gas) of the dive which will also change the total volume of the gas. In the future I will make a more carefull implementation of conservatism and I will leave it upto the user to the user to decide what tank sizes he wants to use.

There is also freedom in the choise of the duration of the decompression stops and each dive computer has its own implementation. Currently I set the fist decompression stop to be proportional to the produce of the depth and the bottom time (depth*time) and I increase its durration at each succeeding  deco stop by 3 minutes. I also decrease the ascent rate. Finding the optimal factor by which the durration of the decompression stops have to increase in order for the diver to reach the surface sooner is something I want to investigate and implement in the future.

For short ar shallow dives where the critical ceiling remains above te water column I add a precautionary safety stop at 3 meters.

The `next_mult3(n)` function inputs a number n returns the next greater multiple of 3 (deco stops are traditionally multiples of 3). I use this function to find the most convenient decompresion stop that is close and below the critical ceiling.

The `altitude_pressure()` function takes the input for the altitue and calculates the basic atmospheric pressure that is later used in the computations.

The object `algo` is composed of the different dictionaries with the parameters for the different versions of the Bulhmann algorithm implementation.

The function `compartment_pressure_initialize()` takes the input of the user for the decompression algorithm and the altitute and initialises all 16 tissue compartments before the start of the dive. It returns an object with 16 entries each being a dictionary with two items one key for nitrogen "N" and another for helium "He" and a corresponding values for the partial pressure of that gas in the corresponding tissue compartment.

The function `gas_loading_descend(depth, rate, fN2, fHe)` takes as inputs  the depth, the descent rate, the ratio of Nitrogen (fN2) and Helium (fHe) in the breathing mix, the altitude, the breathing rate and the initialized tissue compartments. It outputs the updated object with the partial pressures of the innert gases at each tissue compartment, the critical ceiling in meters, the next proposed decompresion stop in meters is the diver decides to abort the dive early and ascend, the end depth after the descend, the gas consumed durring the descent and the dive profile so far in a form of an array with three entries [starting depth, final depth, time ellapsed].

The function `the_dive(t, fN2, fHe, comp)` is used for the horizontal parts of the dive plan, such as the main portion of the dive at the bottom and the decompression stops. It takes as inputs the time duration of the dive at that depth, the ratio of the Nitrogen and Helium in the breathing mix and the all  the output from the previous portion of the dive. The output is again similar to that of he `gas_loading_descend` function.

The `gas_loading_ascend()` is similar to `gas_loading_descend()` but the ascen rate it now takes negative values. The output is agin similar.

The function `build_profile()` uses the above functions to construct a history of depths, deco stops volume of gas breahed untill the the end of the dive. I first call the `gas_loading_descend()` for the descent untill we reach  the target depth and then the `the_dive(t, fN2, fHe, comp)` for the main part of the dive were here t is equal to the bottom time intup o the user. Later I use a while loop and I alternate between `gas_loading_ascend()` and `the_dive(t, fN2, fHe, comp)`, where t in this case is arbitralily set to be 3 + Depth* Bottom time/(300) in the first deco stop and then increeased by 3 minutes at each succeeding deco stop, untill the end depth is equal to 0.
Here I have also implemented some gas switching to assist the decompression in the ascenting part of the dive. The user might find that for certain parameters the dive profile does not end back at the surface. The reason is that I need to increase the time duration of the shallow decompression stops as well perform an gas switches already at the descending part of the dive.

The `plot()` function uses the last element of the output object `build_profile()` which is a list of arrays, each of which looks like [starting depth, final depth, time ellapsed] in order to plot the dive profile using Plotly. I also fill the table with the decompression stops at this point by callin the `loadTableData(items)` function.

The function `total_volume()` helps us compute the total breathing gas used for the dive which also changes according to the redundancy rule we are using, determined by the user input 'conservatism'.

### Logging in / Registering / Logging out / Password Change

Following the problem 'finance', I require the user to log in or regirstering in order to access the the website. An apology is rendered if either input is blank or the passwords do not match.
After logging in I give the user the ability to change the password or log out
to the website

# To do: 
- [ ] Declutter the code. Move functions from index.html
- [ ] Chage the gas_loading_descend function so that you can have a stop for gas changing at descend
- [ ] Keep the position of certain divs as the window changes width
- [ ] Implement the option for Gradient factors and M-values


