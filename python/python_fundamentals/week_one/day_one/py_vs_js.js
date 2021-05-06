//Problem 1
                    function returnAVariable(){
                                var strAndNum = "Day" + 1;
                            var myVariable = 10;
                        return myVariable;
                                                }
        //Let's Log to Console!!!
        console.log(returnAVariable());
































//Problem 2
function ifStatement() {
	var myVariable = 50;
	var bool = false;
	if (myVariable == 99999 && true) {
		myVariable--;
		console.log("What do your elf eyes see?");
	} else if (myVariable == 50) {
		myVariable++;
		console.log("They’re taking the hobbits to Isengard!");
	} else {
		console.log("Tell me where is Gandalf, for I much desire to speak with him.");
	}
	return myVariable;
}
console.log(ifStatement());
























//Problem 3
function forLoops(arr) {
	arr.pop();
	arr.push(6);
	for(var i = 0; i < arr.length; i++) {
		console.log(arr[i]);
    }
	for(var i = 0; i < arr.length; i++) {
		console.log(arr[i]);
	}
}
forLoop([3, 7, 2, 9]);
