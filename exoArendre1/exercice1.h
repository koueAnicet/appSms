#ifndef EXERCICE1_H
#define EXERCICE1_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class exercice1; }
QT_END_NAMESPACE

class exercice1 : public QMainWindow
{
    Q_OBJECT

public:
    exercice1(QWidget *parent = nullptr);
    ~exercice1();

private:
    Ui::exercice1 *ui;
};
#endif // EXERCICE1_H
