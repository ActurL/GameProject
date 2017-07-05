using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace battleTest
{
    class Entity
    {
        public string name;
        public int maxHP;
        public int HP;
        public int minDamage;
        public int maxDamage;

        public Entity()
        {
            
        }

        public string getName()
        {
            return name;
        }

        public int getMaxHP()
        {
            return maxHP;
        }

        public int getHP()
        {
            return HP;
        }

        public void setHP(int HP)
        {
            this.HP = HP;
        }

        public int getMinDamage()
        {
            return minDamage;
        }

        public int getMaxDamage()
        {
            return maxDamage;
        }
    }
}
