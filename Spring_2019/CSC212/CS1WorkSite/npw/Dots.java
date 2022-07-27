package npw;

import java.awt.Color;
import javax.swing.SwingUtilities;
import painter.SPainter;
import shapes.SCircle;

public class Dots {
    private void paintTheImage(){
        SPainter painter = new SPainter("Dots",600,600);
        SCircle yCircle = new SCircle(30);
        SCircle rCircle = new SCircle(10);
        SCircle gCircle = new SCircle(20);
        paintYC(painter,yCircle);
        paintRC(painter,rCircle);
        paintGC(painter,gCircle);
    }
    public Dots() {paintTheImage();}

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable(){
            public void run() { new Dots();}
        });
    }

    private void paintYC(SPainter painter,SCircle circle){
        painter.setColor(Color.YELLOW);
        painter.paint(circle);
    }
    private void paintRC(SPainter painter,SCircle circle){
        painter.setColor(Color.RED);
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mlt(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mlt(circle.diameter());
        painter.paint(circle);
        painter.moveToCenter();
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mrt(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mrt(circle.diameter());
        painter.paint(circle);
        painter.moveToCenter();
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mlt(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mlt(circle.diameter());
        painter.paint(circle);
        painter.moveToCenter();
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mrt(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mrt(circle.diameter());
        painter.paint(circle);
        painter.moveToCenter();
    }
    private void paintGC(SPainter painter,SCircle circle){
        painter.setColor(Color.GREEN);
        painter.mlt(circle.diameter());
        painter.mlt(circle.diameter());
        painter.mlt(circle.diameter());
        painter.mlt(circle.diameter());
        painter.paint(circle);
        painter.moveToCenter();
        painter.mrt(circle.diameter());
        painter.mrt(circle.diameter());
        painter.mrt(circle.diameter());
        painter.mrt(circle.diameter());
        painter.paint(circle);
        painter.moveToCenter();
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.mfd(circle.diameter());
        painter.paint(circle);
        painter.moveToCenter();
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.mbk(circle.diameter());
        painter.paint(circle);
        painter.moveToCenter();
    }
}
