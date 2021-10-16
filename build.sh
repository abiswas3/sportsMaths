# This will be automated eventually- being lazy for now
pandoc -s -c main.css -A footer.html -H main_header.html main.md -o index.html
cd EloTriathlon/ && ./build && cd ../
cd eloExplained/ && ./build && cd ../
cd TriathlonTriva/ && ./build && cd ../
cd ProblemStatement/ && ./build && cd ../
