using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public class Attribute
    {
        public string name;
        public double value;
    }

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void StartButton_Click(object sender, EventArgs e)
        {
            OutBox.Clear();

            List<Attribute> matrixAttr = new List<Attribute>();
            int x = 0;
            int y = 0;
            double min = 0;
            double[,] A1;

            x = int.Parse(Xbox.Text);
            y = int.Parse(Ybox.Text);

            A1 = new double[x, y];
            for (int i = 0, index = 0; i < x; i++)
                for (int j = 0; j < y; j++, index++)
                    A1[i, j] = parseElement(index);

            for (int i = y - x, count = 0; i < y; count++, i++)
            {
                matrixAttr.Add(new Attribute()
                {
                    value = A1[count, y - 1]
                });

                if (i == y - 1)
                    matrixAttr[count].name = "P";
                else
                    matrixAttr[count].name = "x" + i;
            }

            do
            {
                min = 0;
                int colPosition = 0;
                // Find min element in last line and set colPosition
                for (int i = 0; i < y; i++)
                    if (A1[x - 1, i] < 0 && min > A1[x - 1, i])
                    {
                        min = A1[x - 1, i];
                        colPosition = i;
                    }

                double[] tempArray = new double[x - 1];
                // A1[Last col] / A1[colPosition]
                for (int i = 0; i < tempArray.Length; i++)
                    tempArray[i] = A1[i, y - 1] / A1[i, colPosition];

                min = tempArray[0];
                int rawPosition = 0;
                // Find min element and set rawPosition
                for (int i = 0; i < tempArray.Length; i++)
                    if (min > tempArray[i])
                    {
                        min = tempArray[i];
                        rawPosition = i;
                    }

                double num = A1[rawPosition, colPosition];
                // A1[rawPosition] / A1[rawPosition, colPosition]
                for (int i = 0; i < y; i++)
                    A1[rawPosition, i] = A1[rawPosition, i] / num;

                // A1[raws] - A1[rawPosition] * A1[colPosition]
                for (int i = 0; i < x - 1; i++)
                    if (i != rawPosition)
                    {
                        num = A1[i, colPosition];
                        for (int j = 0; j < y; j++)
                            A1[i, j] = A1[i, j] - A1[rawPosition, j] * Math.Abs(num);
                    }

                num = A1[x - 1, colPosition];
                // A1[Last raw] + A1[rawPosition] * A1[colPosition]
                for (int i = 0; i < y; i++)
                    A1[x - 1, i] = A1[x - 1, i] + A1[rawPosition, i] * Math.Abs(num);

                // Change values and rawPosition.name beacause of new basic solution
                for (int i = 0; i < x; i++)
                {
                    matrixAttr[i].value = A1[i, y - 1];

                    if (i == rawPosition)
                        matrixAttr[i].name = "x" + i;
                }

                // Repeat?
                min = 0;
                for (int i = 0; i < y; i++)
                    if (A1[x - 1, i] < 0 && min > A1[x - 1, i])
                        min = A1[x - 1, i];
            } while (min < 0);

            // Sort by Name column
            matrixAttr.Sort((a, b) => {
                if (a.name != "P" && b.name != "P")
                    return a.name.CompareTo(b.name);

                return 0;
                });
            // And print out
            for (int i = 0; i < x; i++)
            {
                OutBox.AppendText(matrixAttr[i].name + " = " + matrixAttr[i].value + "\n");
            }
        }

        private double parseElement(int index)
        {
            return double.Parse(parseLine()[index]);
        }

        private List<string> parseLine()
        {
            return EnterBox.Text.Split(new[] { ' ', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries).ToList();
        }

        private void label1_Click(object sender, EventArgs e)
        {
        }
    }
}