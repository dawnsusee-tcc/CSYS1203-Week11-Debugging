# TCC PYTHON guided debugging - October 28, 2026
Dawn Susee, PhD

## Student path
1. Sign in to GitHub with your existing account.
2. Open the course repository link supplied in Blackboard.
3. Code > Codespaces > Create codespace on main. Use a 2-core machine when offered.
4. Wait for setup. Open accumulator_bug.py.
5. Run the program. The intentional bug prints 5; the expected total is 50.
6. Click the gutter beside the reset inside the loop to set a breakpoint.
7. Run and Debug > select accumulator_bug > Start Debugging.
8. Inspect total and value. The highlighted statement has not executed yet.
9. Step Over the reset. Step Into add_value at its call, then Step Out.
10. Remove the reset inside the loop, save, restart, and verify 50.
11. Remove the breakpoint by clicking it. Stop debugging with the square button.
12. Open https://github.com/codespaces and use the codespace menu > Stop codespace.
Closing the browser tab does not immediately stop the codespace. Stopped spaces retain storage.

The accumulator_fixed version is a reference after discussion. There is no new graded independent activity.

## Instructor preflight
Upload the CONTENTS of this folder to the intended repository root, including .devcontainer and .vscode. Do not upload only this enclosing folder. Supply that repository's real link in Blackboard before class.
Create a fresh codespace, confirm both required extensions finish installing, execute the setup check, run the example, and verify a breakpoint and every stepping control. Repeat this for each language repository. A successful run alone does not verify debugger configuration.
If setup fails during class, students trace on paper while the instructor shares a working debugger or trace demonstration. Keep the 30-minute guided debugging segment.
