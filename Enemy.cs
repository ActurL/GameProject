using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace battleTest
{
    class Enemy : Entity
    {
        private string[][] monsterDetails;
        private string[] monster;
        private Random rand = new Random();
        private string type;

        public Enemy() : base()
        {
            //Takes enemies from a text file. Not sure if I'll keep that format but it works.
            monsterDetails = fileRead("Enemies");
            monster = monsterDetails[rand.Next(monsterDetails.Length)];

            //Assigns values to the enemy's properties
            type = monster[0];
            name = monster[1];
            maxHP = int.Parse(monster[2]);
            minDamage = int.Parse(monster[3]);
            maxDamage = int.Parse(monster[4]);
            HP = maxHP;

        }

        private string[][] fileRead(string fileName)
        {
            //Reads enemy text file
            string[] line;
            string[] fileLines;
            char[] delimeters = { ',' };

            fileLines = System.IO.File.ReadLines(fileName + ".txt").ToArray();
            string[][] separatedFileLines = new string[fileLines.Length][];

            for (int i = 0; i < fileLines.Length; i++)
            {
                line = fileLines[i].Split(delimeters, StringSplitOptions.RemoveEmptyEntries);
                line[line.Length - 1] = line[line.Length - 1].Replace("\n", "");
                separatedFileLines[i] = line;
            }

            return separatedFileLines;
        }

        public string getType()
        {
            return type;
        }
    }
}
