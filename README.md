<h3 align="center"><img src="https://i.imgur.com/5WgMACe.gif" width="200px"></h3>
<p align="center">Generate and change color-schemes on the fly.</p>

<p align="center">
<a href="./LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=V7QNJNKS3WYVS"><img src="https://img.shields.io/badge/donate-paypal-green.svg"></a>
<a href="https://www.jetify.com/devbox/docs/contributor-quickstart/">
    <img
        src="https://www.jetify.com/img/devbox/shield_moon.svg"
        alt="Built with Devbox"
    />
</a>
</p>


<img src="https://i.imgur.com/HhK3LDv.jpg" alt="img" align="right" width="400px">

Pywal is a tool that generates a color palette from the dominant colors in an image. It then applies the colors system-wide and on-the-fly in all of your favourite programs.  

There are currently 5 supported color generation backends, each providing a different palette of colors from each image. You're bound to find an appealing color-scheme.

Pywal also supports predefined themes and has over 250 themes built-in. You can also create your own theme files to share with others.

The goal of Pywal was to be as out of the way as possible. It doesn't modify any of your existing configuration files. Instead it works around them and provides tools to integrate your system as you see fit.

Terminal emulators and TTYs have their color-schemes updated in real-time with no delay. With minimal configuration this functionality can be extended to almost anything running on your system.

## Contribution

### Development Setup

We use Devbox for managing our development environment.
Run `devbox shell` to install the required development dependencies.

### Tests

You can run the test-suite by running:
```
devbox run test
# or
poetry run pytest
```