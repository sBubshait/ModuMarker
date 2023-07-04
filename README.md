# 🚀 ModuMarker 🖍️

Welcome to ModuMarker! 🎉 This delightful little project is your ultimate friend in analyzing scanned answer sheets or OMR sheets. Built with Python and a dash of magic, ModuMarker is configurable, powerful, and friendly. 🧙

## 🌟 Features

- 🌈 Process answer sheets with various shapes of bubbles (circles, rectangles, ellipses).
- 📐 Configurable through a super easy JSON template file which lets you specify the layout of the answer sheet.
- ⚖️ Intelligent threshold-based determination of whether a bubble is filled or not.
- 💖 Written with love and a touch of wizardry in Python.

## 🚀 Getting Started

### ✅ Prerequisites

To run ModuMarker, you'll need:

- Python 3.x 🐍
- OpenCV 📷
- NumPy 🔢

You can install the required libraries using pip (it's like a magic spell! 🪄):

```sh
pip install opencv-python numpy
```

### 🧙‍♂️ Usage

The spell to run ModuMarker is simple. Just use Python to run `main.py` in the `src` directory. You will also need to provide the paths to the image and template file. For example:

```py
    responses = process_answer_sheet("PATH_TO_TEST_IMAGE", "PATH_TO_TEMPLATE")
```

Replace the paths with the correct paths to your image and template file.

We have already set an example for you to try! Go ahead and run main.py! 🧙‍♀️

```sh
python3 main.py
```


### 🎨 Experimentation Kit Included!

Worry not! We have conjured up an empty answer sheet 📄 (`empty.png`) for you to experiment and play around with. Want to try your own spells and incantations? Use the `example.json` as your spell book 📜 and see how ModuMarker dances to your whims. It’s the perfect way to get started on your magical 🧙‍♂️ marking journey!

## 🛠️ Customizing The Template

You can customize the template file (`example.json`) to fit the structure of your answer sheet. It's like crafting your own magic wand! 🪄 Check out the comments in `template.json.txt` to know more about how you can configure it to your needs.

### 🌈 Visualize Before You Finalize!

Hold on! Before your template sets sail ⛵, let's give it a quick check with `visualise.py`. Think of it like your buddy who double-checks if you took the keys 🔑 before leaving home! It colors all the bubbles 🎨 in your template so you can easily see if they're perfectly aligned with your answer sheets. Just a little something to make sure everything is shipshape! 🛳️


## 🙌 Contributing

ModuMarker is open to wizards and witches all around the world. If you have spells, enchantments, or plain ol' code to contribute, feel free to make a pull request! 🚀

## 📜 License

ModuMarker is under the MIT license. See the [LICENSE](LICENSE) for more information.

## 🎉 Have fun marking!

Enjoy ModuMarker and may your answer sheets always be graded with care and magic! ✨