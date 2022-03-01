#include "exercice1.h"
#include "ui_exercice1.h"

exercice1::exercice1(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::exercice1)
{
    ui->setupUi(this);
}

exercice1::~exercice1()
{
    delete ui;
}

