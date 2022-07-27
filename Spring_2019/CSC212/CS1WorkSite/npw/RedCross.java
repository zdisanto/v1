package npw;

import java.awt.Color;
import java.awt.geom.Point2D;
import javax.swing.SwingUtilities;
import painter.SPainter;
import shapes.SRectangle;

public class RedCross {
    public void paintTheImage() {
        SPainter klee = new SPainter("Red Cross",600,600);
        SRectangle line= new SRectangle(500,100);
        klee.setColor(Color.RED);
        klee.paint(line);
        klee.tl();
        klee.paint(line);

        }

        public RedCross() {paintTheImage();}

        public static void main(String[] args) {
            SwingUtilities.invokeLater(new Runnable(){
                public void run() { new RedCross();}
            });
        }
    }
