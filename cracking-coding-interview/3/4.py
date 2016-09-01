def hanoi_tower__recursive(disks, source_tower=1, target_tower=3, auxiliary_tower=2):
    if disks == 1:
        print('Disk {} : {} -> {}'.format(disks, source_tower, target_tower))
        return
    hanoi_tower__recursive(disks-1, source_tower, auxiliary_tower, target_tower)
    print('Disk {} : {} -> {}'.format(disks, source_tower, target_tower))
    hanoi_tower__recursive(disks-1, auxiliary_tower, target_tower, source_tower)

if __name__ == '__main__':
    print('3 disks Hanoi tower')
    hanoi_tower__recursive(3)
    print('4 disks Hanoi tower')
    hanoi_tower__recursive(4)
