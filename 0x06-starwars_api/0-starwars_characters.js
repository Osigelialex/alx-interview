#!/usr/bin/node
const request = require('request');
const process = require('process');

const movieID = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/';
const filmsEndPoint = `${api}films/${movieID}`;

request(filmsEndPoint, (error, response, data) => {
  if (!error && response.statusCode === 200) {
    const json = JSON.parse(data);
    const characterEndPoints = json.characters;

    function printCharacterNames (index) {
      if (index >= characterEndPoints.length) return;

      request(characterEndPoints[index], (charError, charResponse, charData) => {
        if (!charError && charResponse.statusCode === 200) {
          const json = JSON.parse(charData);
          const characterName = json.name;
          console.log(characterName);
        }
      });

      printCharacterNames(++index);
    }

    printCharacterNames(0);
  }
});
