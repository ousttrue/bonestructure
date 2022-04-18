from enum import Enum


class HumanoidBodyParts(Enum):
    Trunk = "Trunk"
    Legs = "Legs"
    LeftArm = "LeftArm"
    LeftFingers = "LeftFingers"
    RightArm = "RightArm"
    RightFingers = "RightFingers"


class HumanoidBone(Enum):
    hips = "hips"
    spine = "spine"
    chest = "chest"
    upperChest = "upperChest"
    neck = "neck"
    head = "head"
    leftEye = "leftEye"
    rightEye = "rightEye"
    jaw = "jaw"
    leftUpperLeg = "leftUpperLeg"
    leftLowerLeg = "leftLowerLeg"
    leftFoot = "leftFoot"
    leftToes = "leftToes"
    rightUpperLeg = "rightUpperLeg"
    rightLowerLeg = "rightLowerLeg"
    rightFoot = "rightFoot"
    rightToes = "rightToes"
    leftShoulder = "leftShoulder"
    leftUpperArm = "leftUpperArm"
    leftLowerArm = "leftLowerArm"
    leftHand = "leftHand"
    rightShoulder = "rightShoulder"
    rightUpperArm = "rightUpperArm"
    rightLowerArm = "rightLowerArm"
    rightHand = "rightHand"
    leftThumbProximal = "leftThumbProximal"
    leftThumbIntermediate = "leftThumbIntermediate"
    leftThumbDistal = "leftThumbDistal"
    leftIndexProximal = "leftIndexProximal"
    leftIndexIntermediate = "leftIndexIntermediate"
    leftIndexDistal = "leftIndexDistal"
    leftMiddleProximal = "leftMiddleProximal"
    leftMiddleIntermediate = "leftMiddleIntermediate"
    leftMiddleDistal = "leftMiddleDistal"
    leftRingProximal = "leftRingProximal"
    leftRingIntermediate = "leftRingIntermediate"
    leftRingDistal = "leftRingDistal"
    leftLittleProximal = "leftLittleProximal"
    leftLittleIntermediate = "leftLittleIntermediate"
    leftLittleDistal = "leftLittleDistal"
    rightThumbProximal = "rightThumbProximal"
    rightThumbIntermediate = "rightThumbIntermediate"
    rightThumbDistal = "rightThumbDistal"
    rightIndexProximal = "rightIndexProximal"
    rightIndexIntermediate = "rightIndexIntermediate"
    rightIndexDistal = "rightIndexDistal"
    rightMiddleProximal = "rightMiddleProximal"
    rightMiddleIntermediate = "rightMiddleIntermediate"
    rightMiddleDistal = "rightMiddleDistal"
    rightRingProximal = "rightRingProximal"
    rightRingIntermediate = "rightRingIntermediate"
    rightRingDistal = "rightRingDistal"
    rightLittleProximal = "rightLittleProximal"
    rightLittleIntermediate = "rightLittleIntermediate"
    rightLittleDistal = "rightLittleDistal"

    def get_part(self) -> HumanoidBodyParts:
        return HUMANOIDBONE_PART_MAP[self]

    def is_finger(self) -> bool:
        return self in (
            HumanoidBone.leftThumbProximal,
            HumanoidBone.leftThumbIntermediate,
            HumanoidBone.leftThumbDistal,
            HumanoidBone.leftIndexProximal,
            HumanoidBone.leftIndexIntermediate,
            HumanoidBone.leftIndexDistal,
            HumanoidBone.leftMiddleProximal,
            HumanoidBone.leftMiddleIntermediate,
            HumanoidBone.leftMiddleDistal,
            HumanoidBone.leftRingProximal,
            HumanoidBone.leftRingIntermediate,
            HumanoidBone.leftRingDistal,
            HumanoidBone.leftLittleProximal,
            HumanoidBone.leftLittleIntermediate,
            HumanoidBone.leftLittleDistal,
            HumanoidBone.rightThumbProximal,
            HumanoidBone.rightThumbIntermediate,
            HumanoidBone.rightThumbDistal,
            HumanoidBone.rightIndexProximal,
            HumanoidBone.rightIndexIntermediate,
            HumanoidBone.rightIndexDistal,
            HumanoidBone.rightMiddleProximal,
            HumanoidBone.rightMiddleIntermediate,
            HumanoidBone.rightMiddleDistal,
            HumanoidBone.rightRingProximal,
            HumanoidBone.rightRingIntermediate,
            HumanoidBone.rightRingDistal,
            HumanoidBone.rightLittleProximal,
            HumanoidBone.rightLittleIntermediate,
            HumanoidBone.rightLittleDistal,
        )


HUMANOIDBONE_PART_MAP = {
    HumanoidBone.hips: HumanoidBodyParts.Trunk,
    HumanoidBone.spine: HumanoidBodyParts.Trunk,
    HumanoidBone.chest: HumanoidBodyParts.Trunk,
    HumanoidBone.upperChest: HumanoidBodyParts.Trunk,
    HumanoidBone.neck: HumanoidBodyParts.Trunk,
    HumanoidBone.head: HumanoidBodyParts.Trunk,
    HumanoidBone.leftEye: HumanoidBodyParts.Trunk,
    HumanoidBone.rightEye: HumanoidBodyParts.Trunk,
    HumanoidBone.jaw: HumanoidBodyParts.Trunk,
    HumanoidBone.leftUpperLeg: HumanoidBodyParts.Legs,
    HumanoidBone.leftLowerLeg: HumanoidBodyParts.Legs,
    HumanoidBone.leftFoot: HumanoidBodyParts.Legs,
    HumanoidBone.leftToes: HumanoidBodyParts.Legs,
    HumanoidBone.rightUpperLeg: HumanoidBodyParts.Legs,
    HumanoidBone.rightLowerLeg: HumanoidBodyParts.Legs,
    HumanoidBone.rightFoot: HumanoidBodyParts.Legs,
    HumanoidBone.rightToes: HumanoidBodyParts.Legs,
    HumanoidBone.leftShoulder: HumanoidBodyParts.LeftArm,
    HumanoidBone.leftUpperArm: HumanoidBodyParts.LeftArm,
    HumanoidBone.leftLowerArm: HumanoidBodyParts.LeftArm,
    HumanoidBone.leftHand: HumanoidBodyParts.LeftArm,
    HumanoidBone.rightShoulder: HumanoidBodyParts.RightArm,
    HumanoidBone.rightUpperArm: HumanoidBodyParts.RightArm,
    HumanoidBone.rightLowerArm: HumanoidBodyParts.RightArm,
    HumanoidBone.rightHand: HumanoidBodyParts.RightArm,
    HumanoidBone.leftThumbProximal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftThumbIntermediate: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftThumbDistal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftIndexProximal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftIndexIntermediate: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftIndexDistal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftMiddleProximal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftMiddleIntermediate: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftMiddleDistal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftRingProximal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftRingIntermediate: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftRingDistal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftLittleProximal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftLittleIntermediate: HumanoidBodyParts.LeftFingers,
    HumanoidBone.leftLittleDistal: HumanoidBodyParts.LeftFingers,
    HumanoidBone.rightThumbProximal: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightThumbIntermediate: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightThumbDistal: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightIndexProximal: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightIndexIntermediate: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightIndexDistal: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightMiddleProximal: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightMiddleIntermediate: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightMiddleDistal: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightRingProximal: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightRingIntermediate: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightRingDistal: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightLittleProximal: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightLittleIntermediate: HumanoidBodyParts.RightFingers,
    HumanoidBone.rightLittleDistal: HumanoidBodyParts.RightFingers,
}