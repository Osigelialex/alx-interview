#!/usr/bin/node
const request = require('request');

const getCharacterData = async (movieID) => {
  const api = 'https://swapi-api.alx-tools.com/api/';
  const movieEndPoint = `${api}films/${movieID}`;
  const resp = await new Promise((resolve, reject) => {
    request(movieEndPoint, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
  const data = JSON.parse(resp);
  const characterEndPoints = data.characters;
  return characterEndPoints;
};

const printCharacterNames = async (characterEndPoints) => {
  for (const endpoint of characterEndPoints) {
    const resp = await new Promise((resolve, reject) => {
      request(endpoint, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });
    const data = JSON.parse(resp);
    const characterName = data.name;
    console.log(characterName);
  }
};

const main = async () => {
  const movieID = process.argv[2];
  const characterData = await getCharacterData(movieID);
  await printCharacterNames(characterData);
};

main().catch(error => {
  console.error('An error occurred:', error);
});
