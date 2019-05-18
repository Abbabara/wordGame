$(document).ready(function() {
    //Get existing url
    var userWord = document.getElementById("userWord")
    var gameField = $('div#gameContainer').find('div#box1');
    var strOut = "";

    $('.letterBox').on('click', function(event) {

        //A letter tile was clicked, copying its letter
        var letterInBox = $(this).find('h1')[0].innerText;
        strOut += letterInBox;
        //New box for chosen tile (X) and setting its content
        let letter = document.createElement("div");
        letter.className = "chosenLetter";
        var letterVal = document.createElement("h2");
        var numVal = document.createElement("p");
        letterVal.innerHTML = letterInBox;
        numVal.innerHTML = $(this).find('h3')[0].innerText;
        letterVal.setAttribute("style", "pointer-events: none");
        numVal.setAttribute("style", "pointer-events: none");
        letter.append(letterVal, numVal);

        //Saving the tile for X tile as a variable so its visibility can be toggled
        var squareSelected = event.currentTarget;
        squareSelected.setAttribute("style", "visibility: hidden");
        //When X is clicked, find its location and cut it from the output string
        letter.onclick = (e) => {
            var childIndex = -1;
            for(var child = e.target; child.previousSibling != null; child = child.previousSibling){
                childIndex++;
            }
            squareSelected.setAttribute("style", "visibility: block");
            strOut = strOut.slice(0, childIndex) + strOut.slice(childIndex+1);
            $(e.target).remove();
            userWord.setAttribute("value", strOut);
        };
        //Adding X to the game field
        gameField.find('div.gameBoard').append(letter);
        // changing the href attrinbute
        userWord.setAttribute("value", strOut)
    });

});


