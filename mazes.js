//always going left from BLockly


while (notDone()) {
  if (isPathLeft()) {
    turnLeft();
    moveForward();
  }
  if (isPathForward()) {
    moveForward();
  } else {
    if (isPathRight()) {
      turnRight();
    } else {
      turnRight();
      turnRight();
    }
  }
}
