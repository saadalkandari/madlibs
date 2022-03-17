# madlibs

## Setup

### New Directory

1. Go into the `Development` directory using `cd`.
2. Create a new directory called `python` using `mkdir`.

## Fork & Clone

1. Fork [this repository](https://github.com/JoinCODED/madlibs), which means to make a copy of the repository under your account. You can do this by clicking the button on the top-right corner of the page that says "Fork". The button looks like this:
    ![Fork Button](https://imgur.com/KmH4Fp4.jpg)
2. Activate the GitHub Actions by going to the Actions tab and clicking the big green button.
    ![GitHub Action](https://i.gyazo.com/4ad622c46ce2fdb8ffe4dad63e206d47.gif)
4. Go back to the main repository page by clicking the Code tab on the top-left corner.
    ![Code](https://i.gyazo.com/e666afa70fd87e36cf8a82c24011811f.gif)
5. Click the green button on the right that says "Clone or download," then copy the URL in the popup by clicking the copy button to the right of the URL.
    ![Clone](https://i.gyazo.com/5129e26ff760d6a027a6df253e5f0584.gif)
6. In your `python` directory you just made, clone this repository with this command: `git clone PASTE_URL_HERE`. In this example above, the command would be `git clone https://github.com/msharydemo/madlibs.git`

You'll do these same steps for every task from now on all throughout the bootcamp.

Once you cloned it, you'll see a new directory inside your `python` directory named "madlibs". This is the git repository you just cloned. Inside you'll find a file named "madlibs.py." This is where you'll be writing the code for this task. You can ignore all the other files inside.

In "madlibs.py", you'll find an empty function called `main()`. Write all your code for this task inside this function.

## Task 

In this task, the user should be given a story with gaps that the user should fill to complete the story. So basically a game of mad libs.

Example:
```
Mad libs where libs get mad.
Start below:

Enter a number from 1 to 12: 6
Enter a noun (plural): dolls
Enter a name: stephen sedoll
Enter any sentence: the future is made of dolls
Enter a verb: shake my head

The story goes...

It was 6 o'clock when I heard a knock at the door.
I opened the door and there was a box full of dolls with a note saying "From Mr. Stephen Sedoll."
Just as I closed the door I heard a scream "THE FUTURE IS MADE OF DOLLS."
I froze in place and all I could do was shake my head.
```

The user enters the number `6`, the plural noun `dolls`, the name `stephen sedoll`, the sentence `the future is made of dolls`, and the verb `shake my head`. Then the story at the end is generated automatically based on the user's input.

### Task Steps:

* Use the story in the example above for the user to complete. The values that need to be filled by the user's input are:
    * `time`
    * `items`
    * `name`: When printing the name to the user, the first letter of each word should be capitalized. See the example above.
    * `scream`: When printing the scream to the user, all the letters in the scream have to be capitalized. See the example above.
    * `action`
* Add the file `madlibs.py` to the git repository, commit changes, and push your code to the remote repository.

Hint: You will need [string methods](https://www.w3schools.com/python/python_ref_string.asp).
