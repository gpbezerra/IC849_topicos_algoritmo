enum Colors {
    white,
    orange,
    green,
    red,
    yellow,
    blue
}

// proccurar se tem como limitar o tamanho do array
type Face = {
    positions: Colors[]
    neighbours?: Face[]
}

type OperationSet = {
    faces: Face[]
    positions: number[]
    affectedFace: Face
}

export {Colors, Face, OperationSet}