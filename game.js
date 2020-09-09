class Game {
    constructor(difficulty){
        this.diff = difficulty;
        this.status = false;
    }
    boardCreation(){
        if (this.diff == 0){
            this.Xdim = 10;
            this.Ydim = 8;
            this.diffMult = 6;
        } else if (this.diff == 1){
            this.Xdim = 12;
            this.Ydim = 10;
            this.diffMult = 5.5;
        } else if (this.diff == 2){
            this.Xdim = 20;
            this.Ydim = 15;
            this.diffMult = 5;
        }
        this.mineGen();
        this.numGen();
        this.printTable();
    }
    currentPlay(lastPos){
        this.lastPos = lastPos;
        let id = '#' + this.lastPos[0] + '-' + this.lastPos[1];
        if (this.mineField[parseInt(this.lastPos[0])][parseInt(this.lastPos[1])] == 1){
            $('#tablePos').prepend('You hit a mine. You loose.');
            $(id).css('background-color', 'red');
            $(id).css('color', 'black');
            this.reset();
            $(id).on('mousedown', function(){
                $(this).css('background-color', 'red');
            });
            $('.tableBut').click(function(){
                return false;
            });
        } else {
            this.numberMoves = this.numberMoves + 1;
            $(id).css('background-color', '#dbd4d4');
            $(id).css('cursor', 'default');
            $(id).css('color', 'black');
            $(id).unbind();
            if ((this.Xdim*this.Ydim - this.numMines) == this.numberMoves && !this.status){
                this.status = true;
                $('#tablePos').prepend('Congratulations, you Won.');
                this.reset();
                $('.tableBut').click(function(){
                    return false;
                });
            }
            if (this.numTable[this.lastPos[0]][this.lastPos[1]] == 0){
                this.autofill(lastPos);
            }
        }
    }
    reset(){
        $('#tablePos').css('border','white 2px dashed');
        $('#difficulty').show();
        $('.tableBut').unbind();
        $('.tableBut').css('cursor', 'default');
        $('.tableBut').on('mousedown', function(){
            $(this).css('background-color', '#dbd4d4');
        });
        $('#btm').hide();
    }
    printTable(){
        let table = '<table>';
        for (let j = 0; j < this.Ydim; j++){
            table += '<tr>';
            for (let i = 0; i < this.Xdim; i++){
                table += '<td class=\'tableBut\' id=\'' + j + '-' + i + 
                '\'><span style=\'display: none;\'>AA' +
                 j + ',' + i + 'BB</span><span id=\'S' + j + '-' + i + 
                 '\'></span></td>';
            }
            table += '</tr>';
        }
        table += '</table>';
        $('#tablePos').html(table);
        $('.tableBut').mousedown(function(event){
            let lastPos = $(this).html();
            let n = lastPos.search("AA");
            let m = lastPos.search("BB");
            lastPos = lastPos.substr(n+2, m-n-2);
            lastPos = lastPos.split(',');
            switch (event.which) {
                case 1:
                    $(this).html(game.numTable[parseInt(lastPos[0])][parseInt(lastPos[1])]);
                    game.currentPlay(lastPos);
                    break;
                case 3:
                    game.check(lastPos);
                    break;
            }
            
        })
    }
    check(lastPos){
        let id = '#S' + lastPos[0] + '-' + lastPos[1];
        if ($(id).html() == ''){
            console.log(id);
            $(id).html('P');
            id = '#' + lastPos[0] + '-' + lastPos[1];
            $(id).css('background-color', 'blue');
            $(id).css('color', 'white');
        } else {
            $(id).html('');
            id = '#' + lastPos[0] + '-' + lastPos[1];
            $(id).css('background-color', '#dbd4d4');
            $(id).css('color', 'black');
        }
    }
    mineGen(){
        this.numMines = Math.floor(this.Xdim*this.Ydim/this.diffMult);
        this.numberMoves = 0;
        let deployedMines = 0;
        let mineField = [];
        let mineRow = [];
        let numTable = [];
        let numRow = [];
        for (let j = 0; j < this.Ydim; j++){
            for (let i = 0; i < this.Xdim; i++){
                mineRow[i] = 0;
                numRow[i] = ' ';
            }
            mineField[j] = mineRow;
            mineRow = [];
            numTable[j] = numRow;
            numRow = [];
        }
        this.numTable = numTable;
        let row, column;
        while (deployedMines < this.numMines){
            row = Math.floor(Math.random() * this.Ydim);
            column = Math.floor(Math.random() * this.Xdim);
            if (mineField[row][column] == 0){
                mineField[row][column] = 1;
                deployedMines++;
            } else {
                continue;
            }
        }
        this.mineField = mineField;
    }
    numGen(){
        for (let j = 0; j < this.Ydim; j++){
            for (let i = 0; i < this.Xdim; i++){
                if (this.mineField[j][i] == 1){
                    this.numTable[j][i] = 'X';
                } else {
                    this.mineCalc(j,i);
                }
            }
            console.log(this.numTable[j]);
        }
    }
    mineCalc(row,column){
        let sum = 0;
        let lb = column - 1;
        let rb = column + 1;
        let ub = row - 1;
        let db = row + 1;
        let Jmin = -1;
        let Jmax = 2;
        let Imin = -1;
        let Imax = 2;
        if (lb < 0){ Imin = 0;}
        if (rb > this.Xdim - 1){ Imax = 1;}
        if (ub < 0){ Jmin = 0;}
        if (db > this.Ydim - 1){ Jmax = 1;}
        for (let j = Jmin; j < Jmax; j++){
            for (let i = Imin; i < Imax; i++){
                sum += this.mineField[row+j][column+i];
            }
        }
        this.numTable[row][column] = sum;
    }
    autofill(lastPos){
        let row = parseInt(lastPos[0]);
        let column = parseInt(lastPos[1]);
        let lb = column - 1;
        let rb = column + 1;
        let ub = row - 1;
        let db = row + 1;
        let Jmin = -1;
        let Jmax = 2;
        let Imin = -1;
        let Imax = 2;
        if (lb < 0){ Imin = 0;}
        if (rb > this.Xdim - 1){ Imax = 1;}
        if (ub < 0){ Jmin = 0;}
        if (db > this.Ydim - 1){ Jmax = 1;}
        let id;
        for (let j = Jmin; j < Jmax; j++){
            for (let i = Imin; i < Imax; i++){
                if (j != 0 || i != 0){
                    id = '#' + (row + j) + '-' + (column + i);
                    if (this.numTable[row + j][column + i] == 0 && $(id).html() != '0'){
                        $(id).unbind();
                        $(id).html(this.numTable[parseInt(row)][parseInt(column)]);
                        this.numberMoves = this.numberMoves + 1;
                        $(id).css('background-color', '#dbd4d4');
                        $(id).css('cursor', 'default');
                        $(id).css('color', 'black');
                        console.log([row + j,column + i]);
                        this.autofill([row + j,column + i]);
                    } else if (this.mineField[row + j][column + i] == 0){
                        if ($(id).html() == '0'){
                            continue;
                        } else if ($(id).html() != '' + this.numTable[parseInt(row + j)][parseInt(column + i)]){
                            $(id).unbind();
                            $(id).css('background-color', '#dbd4d4');
                            $(id).css('cursor', 'default');
                            $(id).css('color', 'black');
                            console.log([row + j,column + i]);
                            $(id).html(this.numTable[parseInt(row + j)][parseInt(column + i)]);
                            this.numberMoves = this.numberMoves + 1;
                            continue;
                        }
                    }
                }
            }
        }
        if ((this.Xdim*this.Ydim - this.numMines) == this.numberMoves && !this.status){
            this.status = true;
            $('#tablePos').prepend('Congratulations, you Won.');
            this.reset();
            $('.tableBut').click(function(){
                return false;
            });
        }
    }
}

let a = $('button');
var game;
$('#tablePos').bind("contextmenu",function(e){
    return false;
});
$('#btm').hide();
for (let i = 0; i < a.length; i++){
    $('.difInd').eq(i).click(function(){
        $('#tablePos').css('border','none');
        $('#tablePos').show();
        game = new Game(i);
        $('#difficulty').hide();
        $('#btm').show();
        game.boardCreation();
    })
};
$('body').height($(window).height());
$('#btm').click(function(){
    $('#difficulty').show();
    $('#btm').hide();
    $('#tablePos').hide();
});