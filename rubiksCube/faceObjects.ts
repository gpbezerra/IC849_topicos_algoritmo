import {Face, Colors} from "./cubeType.ts"

// 1 - Branco 
const whiteFace: Face = {
    positions: Array(9).fill(Colors.white),
}

// 2 - Laranja
const orangeFace: Face = {
    positions: Array(9).fill(Colors.orange)
}

// 3 - Verde
const greenFace: Face = {
    positions: Array(9).fill(Colors.green)
}

// 4 - Vermelho
const redFace: Face = {
    positions: Array(9).fill(Colors.red)
}

// 5 - Amarelo
const yellowFace: Face = {
    positions: Array(9).fill(Colors.yellow)
}

// 6 - Azul
const blueFace: Face = {
    positions: Array(9).fill(Colors.blue)
}

whiteFace.neighbours = [orangeFace, greenFace, redFace, blueFace];

export { whiteFace, orangeFace, greenFace, redFace, yellowFace, blueFace}