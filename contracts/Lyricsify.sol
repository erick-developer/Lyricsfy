pragma solidity >=0.4.21 <0.6.0;

contract Lyricsify {
    // Contract owner
    address public owner;

    // Lyrics
    address[] public lyricsOwner;
    mapping(address => string) lyrics;

    // Events
    event StoreLyric(string lyric);

    constructor() public {
        owner = msg.sender;
    }

    function getLyricByIndex(uint8 _idx) public view returns(string memory) {
        return lyrics[lyricsOwner[_idx]];
    }

    function getUsersCount() public view returns(uint) {
        return lyricsOwner.length;
    }

    function setLyricForSender(string memory _lyric) public {
        lyrics[msg.sender] = _lyric;
        lyricsOwner.push(msg.sender);
        emit StoreLyric(_lyric);
    } 
}