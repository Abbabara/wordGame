$(document).ready(function() {
    //Get existing url
    var userWord = document.getElementById("userWord")
    var gameField = $('div.gameContainer').find('div.box1');
    var strOut = "";

    $('.logoContainer').on('click', function(event) {
        console.log('logo container clicked');
    });

    $('.letterBox').on('click', function(event) {

        //A letter tile was clicked, getting its letter
        var letterInBox = $(this).find('h1')[0].innerText;
        //console.log(letterInBox);
        strOut += letterInBox;

        let letter = document.createElement("div");
        letter.className = "chosenLetter";
        letter.innerText = letterInBox;

        var squareSelected = event.currentTarget;
        squareSelected.setAttribute("style", "visibility: hidden");

        letter.onclick = (e) => {
            var childIndex = -1;
            for(var child = e.target; child.previousSibling != null; child = child.previousSibling){
                childIndex++;
            }
            squareSelected.setAttribute("style", "visibility: block");
            strOut = strOut.slice(0, childIndex) + strOut.slice(childIndex+1);
            $(e.target).remove();
        };

        gameField.find('div.gameBoard').append(letter);
        // changing the href attrinbute
        userWord.setAttribute("value", strOut)
    });

});


