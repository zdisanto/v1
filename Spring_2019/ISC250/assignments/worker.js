importScripts('timer.js');

const DEF_QUANTUM = 500;
let workP = false;
let timer = null;
let quantum = DEF_QUANTUM;

onmessage = function(e) {
   if (e.data.msg == "start") {
      if (!workP) {
         i = 0;
         workP = true;
         if (!timer) {
            timer = new time.Timer(quantum, quantum, slice);
         }
         timer.start();
      }
   } else if (e.data.msg == "stop") {
      workP = false;
      if (timer) {
         timer.stop();
      }
   } else if (e.data.msg == "resume") {
      if (!workP) {
         workP = true;
         if (timer) {
            timer.stop();
            timer.start();
         }
      }
   } else if (e.data.msg == "pause") {
      workP = false;
      if (timer) {
         timer.stop();
      }
   } else if (e.data.msg == "quantum") {
      quantum = e.data.value;
      if (timer) {
         timer.stop();
      }
      timer = new time.Timer(quantum, quantum, slice);
      if (workP) {
         timer.start();
      }
   } else {
      console.log("invalid message " + e.data.msg);
   }
}

var i = 0;

function slice() {
   i = i + 1;
   var msg = {};
   msg.msg = 'quote';
   msg.value = i;
   postMessage(msg);
}
