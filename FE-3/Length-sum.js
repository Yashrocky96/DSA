// Given objects in ft and inch formats the following class
// performs addition

class Length {
    constructor (ft, inch) {
        // initializes ft and inch
         this.ft = ft;
         this.inch = inch;
        //  executes at object initialization
         this.isValidObject = () => {
              if (this.ft >= 0 && this.inch >= 0) {
                   return true
              } else return false
         };
         this.isValidObject();
    }
    addLength(lengthObj) {
         let [totFt, totInch] = [0, 0]
         if (this.isValidObject() && 
              lengthObj.isValidObject()) {
                   // Convert ft to inches and gets total inches
                   totInch = ((this.ft + lengthObj.ft) * 12) + this.inch + lengthObj.inch;
                   // Divides to get the feets and % to get the inches
                   totFt = Math.floor(totInch/12);
                   totInch %= 12;
         } 
         return [totFt, totInch]
    }
}

const length1 = new Length(5, 11) //corresponding to 5 ft 11 inches

const length2 = new Length(2, 8) // corresponding to 2 ft 8 inches.

const sum = length1.addLength(length2)

module.exports = Length;