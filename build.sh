# This will be automated eventually- being lazy for now
pandoc -s -c main.css -A footer.html -H header.html main.md -o index.html
cd ProblemStatement/ && ./build && cd ../
cd TommyRank/ && ./build && cd ../
cd eloExplained/ && ./build && cd ../
cd PTO_scoring && ./build && cd ../
cd PrimoRank/ && ./build && cd ../
cd TDF_VELO/ && ./build && cd ../