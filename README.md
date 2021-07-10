# SDL4Snap *!*

SDL4Snap *!*  is a Snap *!*  library with a minimal implementation of the modeling [Specification and Description Language (SDL)](http://www.sdl-forum.org/SDL) in [Snap *!*](http://snap.berkeley.edu) and [Snap4Arduino](http://snap4arduino.rocks).

### (JavaScript extensions must be ticked)

## Try it at: [Hello World!](https://snap.berkeley.edu/snap/snap.html#open:https://raw.githubusercontent.com/pixavier/sdl4snap/master/examples/SDL2Snap-PingPong.xml)

The PingPong example can be considered the ["Hello World"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) of a SDL based multi-agent system. An online runnable example can be found [here](https://snap.berkeley.edu/snap/snap.html#open:https://raw.githubusercontent.com/pixavier/sdl4snap/master/examples/SDL2Snap-PingPong_local.xml).  

## PingPong SDL model

![PingPong SDL model](img/ping_pong_sdl.png)

To import the PingPong SDL model into [UMLetino](https://www.umletino.com), select and copy the following URL to the clipboard, and then paste it when "File Import":

    https://raw.githubusercontent.com/pixavier/sdl4snap/master/examples/PingPong_SDL.uxf


If you just want to import the SDL palette into [UMLetino](https://www.umletino.com), select and copy the following URL to the clipboard, and then paste it when "File Import":

    https://raw.githubusercontent.com/pixavier/mqtt4snap/master/mqtt-standalone.xml


## Usage and blocks

Start from the HelloWorld example, and delete the blocks you will not use. Each agent (sprite) has some atributes (local variables) that are needed by the SDL engine, such as "SDL signal input queue" and "SDL state".

To create new processes, duplicate a similar one instead creating it from scratch.

##
Here you can see the Snap *!* translation of the PingPong example:
###

![Ping Pong Snap *!* implementation](img/ping_pong_snap.png)


### Using PubSub architecture to support distributed messaging

The scheme of processes communication is described in the classic SDL Forum [SDL-88 Tutorial](https://www.sdl-forum.org/sdl88tutorial/4.ProcessCommunication/4.1_Signal_input_queue.htm) SDL Tutorial.
 
![Process communication](img/ProcessCommunication.png)

SDL4Snap *!* can use MQTT to support distributed messaging over a network. The [MQTT4Snap *!*](https://github.com/pixavier/mqtt4snap) extension lets send/receive messages via the MQTT protocol, hence agents (blocks and processes) can run distributed among Snap *!* Internet-connected browsers. MQTT4Snap *!* "pub" and "sub" blocks, combined to the "send signal" block. 

[MQTT](https://en.wikipedia.org/wiki/MQTT) based systems can be combined with other protocols like [HTTP-REST](https://en.wikipedia.org/wiki/Representational_state_transfer) or [OPC-UA](https://opcfoundation.org/resources/brochures) with another no/low-code tools like [Node-RED](https://nodered.org).


