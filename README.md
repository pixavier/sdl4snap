# SDL4Snap *!*

SDL4Snap *!*  is a Snap *!*  library with a minimal implementation of the modeling Specification and Description Language [(SDL)](http://www.sdl-forum.org/SDL) in [Snap *!*](http://snap.berkeley.edu) and [Snap4Arduino](http://snap4arduino.rocks).

## Try it at: [Hello World!](https://snap.berkeley.edu/snap/snap.html#open:https://raw.githubusercontent.com/pixavier/sdl4snap/master/examples/SDL2Snap-PingPong.xml)

The PingPong example can be considered the ["Hello World"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) of a SDL based multi-agent system. An online runnable example can be found [here](https://snap.berkeley.edu/snap/snap.html#open:https://raw.githubusercontent.com/pixavier/sdl4snap/master/examples/SDL2Snap-PingPong_local.xml).  

SDL4Snap *!* can run in distributed mode using the [MQTT4Snap *!*](https://github.com/pixavier/mqtt4snap) library, that lets send/receive messages via the MQTT protocol.
[MQTT](https://en.wikipedia.org/wiki/MQTT) based systems can be combined with other protocols like [HTTP-REST](https://en.wikipedia.org/wiki/Representational_state_transfer) or [OPC-UA](https://opcfoundation.org/resources/brochures) with another no/low-code tools like [Node-RED](https://nodered.org).


## PingPong SDL model

![PingPong SDL model](img/ping_pong_sdl.png)

[UMLetino](https://www.umletino.com) file of the SDL model is downloadable (Save as ...) [here](https://raw.githubusercontent.com/pixavier/sdl4snap/master/examples/PingPong_SDL.uxf).

## Usage and blocks

Start from the HelloWorld example, and delete the blocks you will not use. Each agent (sprite) has some atributes (local variables) that are needed by the SDL engine, such as "SDL signal input queue", "SDL state" and "SDL transition ended".
If you are developing a non distributed system (no network), use always the block "SDL send local signal" instead "SDL send signal" (the last one uses MQTT).
To create new processes, duplicate a similar one instead creating it from scratch.

##
Here you can see the Snap *!* translation of the PingPong example.
###

<!-- ![Minimal example](img/ping_pong_snap.png)  -->


### Using PubSub architecture to support distributed messaging

The scheme of processes communication is described in the classic SDL Forum [SDL-88 Tutorial](https://www.sdl-forum.org/sdl88tutorial/4.ProcessCommunication/4.1_Signal_input_queue.htm) SDL Tutorial.
SDL4Snap *!* uses MQTT as the base mechanism to support distributed messaging. The [MQTT4Snap *!*](https://github.com/pixavier/mqtt4snap) extension has been used for this purpose. With SDL4Snap *!*, agents (blocks and processes) can run distributed among Snap *!* Internet connected browsers.  
 
![Process communication](img/ProcessCommunication.png)



