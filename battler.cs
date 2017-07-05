using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace battleTest
{
    public partial class battleWindow : Form
    {
        public battleWindow()
        {
            InitializeComponent();

            //Placeholder, just inventory for show. Need item class, subclasses for weapons etc.
            dgvInventory.Rows.Add("Rusty Sword", "x1");
            dgvInventory.Rows.Add("Small Healing Potion", "x5");
            dgvInventory.Rows.Add("Beaten Shield", "x1");

            //Again, placeholder. Creates random enemy.
            Enemy enemey = new Enemy();

            //Displays health. I'll move that to a proc so I can run it after attacks too.
            setHealthLabel(enemey.getHP(), enemey.getMaxHP(), lblMonsterHP);
            setHealthLabel(20, 20, lblPlayerHP);

            //formatting combobox
            populateComboBox();
            cmbItemToUse.SelectedIndex = 0;
            rtbOutput.AppendText("A wild " + enemey.getName() + " appeared!");
        }

        private void populateComboBox()
        {
            //proc to move inventory items into combobox
            for (int i = 0; i < dgvInventory.RowCount; i++)
            {
                cmbItemToUse.Items.Add(dgvInventory.Rows[i].Cells[0].Value);
            }
        }

        private void setHealthLabel(int HP, int maxHP, Label label)
        {
            //displays HP
            label.Text = HP + "/" + maxHP;
        }
    }
}
