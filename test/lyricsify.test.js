const Lyricsify = artifacts.require("./Lyricsify"),
      truffleAssert = require('truffle-assertions');


contract("Lyricsify", async(accounts) => {
  it("should store a given lyric for a user", async () => {
    const testLyric = "Por la esquina de un viejo barrio lo vi pasar, con el tumbao que llevan los wapos a caminar."
    const { setLyricForSender } = await Lyricsify.deployed();
    const response = await setLyricForSender(testLyric, {from: accounts[0]});
    truffleAssert.eventEmitted(response, 'StoreLyric', ({lyric}) => {
      return testLyric === lyric;
    });
  });
  it("should retrieve a lyric given a index of a user", async () => {
    // STORE
    const testLyric = "Por la esquina de un viejo barrio lo vi pasar, con el tumbao que llevan los wapos a caminar."
    const { setLyricForSender } = await Lyricsify.deployed();
    const responseLyricForSender = await setLyricForSender(testLyric, {from: accounts[0]});

    // RETRIEVE
    const idx = 0;
    const { getLyricByIndex } = await Lyricsify.deployed();
    const storedLyric = await getLyricByIndex(idx, {from: accounts[0]});
    assert.equal(testLyric, storedLyric);
  });
});