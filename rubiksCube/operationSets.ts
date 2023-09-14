import {OperationSet} from "./cubeType.ts"
import { whiteFace, orangeFace, greenFace, redFace, yellowFace, blueFace } from './faceObjects.js'
// Escolher 3 faces que não sejam inversas umas das outras, e fazer delas pontos de vista. Para cada um desses pontos de vista, haverão 4 operationSets.
// Os pontos de vista serão importantes para as operações 

const leftColumn: OperationSet = {
    faces: [whiteFace, orangeFace, yellowFace, blueFace],
    positions: [2, 5, 8],
    affectedFace: redFace
}

const rightColumn: OperationSet = {
    faces: [whiteFace, orangeFace, yellowFace, blueFace],
    positions: [0, 3, 6],
    affectedFace: orangeFace
}

const topRow: OperationSet = {
    faces: [whiteFace, redFace, yellowFace, orangeFace],
    positions: [0, 1, 2],
    affectedFace: blueFace
}

const bottomRow: OperationSet = {
    faces: [whiteFace, redFace, yellowFace, orangeFace],
    positions: [6, 7, 8],
    affectedFace: greenFace
}