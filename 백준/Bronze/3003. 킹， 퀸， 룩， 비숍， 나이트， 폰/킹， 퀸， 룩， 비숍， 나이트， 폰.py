nowKing, nowQueen, nowRook, nowBishop, nowKnight, nowPawn = map(int, input().split())
correctKing, correctQueen, correctRook, correctBishop, correctKnight, correctPawn = 1, 1, 2, 2, 2, 8

print(correctKing - nowKing,
      correctQueen - nowQueen,
      correctRook - nowRook,
      correctBishop - nowBishop,
      correctKnight - nowKnight,
      correctPawn - nowPawn)