const time = (function() {
   const MIN_TICK = 125;
   function T(a, b, f) {
      a = Math.abs(a); b = Math.abs(b);
      if (a*1 > b*1) { var t = a; a = b; b = t; }
      if (b - a < MIN_TICK) { b = a*1 + MIN_TICK; }
      this.a = a; this.b = b;
      this.f = f;
      this.timerID = null;
   }

   T.prototype.start = function() {
      this.tick();
   }

   T.prototype.stop = function() {
      clearTimeout(this.timerID);
   }

   T.prototype.tick = function() {
      if (typeof this.f === 'function')
         this.f();
      var time = Math.floor(Math.random()*(this.b-this.a) + this.a);
      if (this.timerID) clearTimeout(this.timerID);
      var this_ = this;
      this.timerID = setTimeout(function(){this_.tick();},time);
   }

   return {
      Timer: T
   }
})();
